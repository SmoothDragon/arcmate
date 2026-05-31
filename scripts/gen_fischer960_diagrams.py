#!/usr/bin/env python3
"""Generate Fischer Random 960 step diagrams via Wikipedia {{Chess diagram}}."""

from __future__ import annotations

import sys
from pathlib import Path

from wikipedia_chess_diagram import (
    build_chess_diagram_wikitext,
    render_diagram_svg,
)

OUT_DIR = Path(__file__).resolve().parents[1] / "docs" / "fischer960"
WIKI_DIR = OUT_DIR / "wikitext"
CACHE_DIR = OUT_DIR / "commons-cache"
SIZE = 32

# White pieces (l = light side per Module:Chessboard/Chess)
PIECE = {"K": "kl", "Q": "ql", "R": "rl", "B": "bl", "N": "nl"}


def label(n: str) -> str:
    return f"x{n}"


def rank1_from_state(files: dict[int, dict]) -> dict[int, str]:
    row: dict[int, str] = {}
    for f in range(1, 9):
        info = files.get(f, {})
        if info.get("piece"):
            row[f] = PIECE[info["piece"]]
        elif info.get("label"):
            row[f] = label(info["label"])
        else:
            row[f] = "  "
    return row


def write_step(
    path: Path,
    wiki_path: Path,
    rank1: dict[int, str],
    caption: str,
) -> None:
    wikitext = build_chess_diagram_wikitext(
        rank1,
        header="",
        footer="",
        size=SIZE,
        numbers="neither",
        letters="bottom",
    )
    wiki_path.write_text(wikitext + "\n", encoding="utf-8")
    render_diagram_svg(
        rank1,
        path,
        cache_dir=CACHE_DIR,
        size=SIZE,
        caption=caption,
    )


def empty_rank() -> dict[int, dict]:
    return {f: {} for f in range(1, 9)}


def subtract_roll_expr(roll: int, subtract: int, hi: int) -> str:
    """e.g. 16, 5, 5 → '16 - 3*5 = 1' (repeated subtraction shown as n×step)."""
    count = 0
    value = roll
    while value > hi:
        value -= subtract
        count += 1
    return f"{roll} - {count}*{subtract} = {value}"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    WIKI_DIR.mkdir(parents=True, exist_ok=True)

    steps: list[tuple[str, dict[int, dict], str]] = [
        (
            "step-01-empty",
            {f: {"label": str(f)} for f in range(1, 9)},
            "Step 1 — empty rank 1; squares numbered 1–8 (d8)",
        ),
        (
            "step-02-queen",
            {
                **{f: {"label": str(f)} for f in range(1, 9) if f != 6},
                6: {"piece": "Q"},
            },
            "Step 2 — d8 = 6 → Queen on f",
        ),
        (
            "step-03-dark-labels",
            {
                **{**empty_rank(), 6: {"piece": "Q"}},
                **{f: {"label": lb} for f, lb in [(1, "1"), (3, "2"), (5, "3"), (7, "4")]},
            },
            "Step 3 — label empty dark squares 1–4",
        ),
        (
            "step-04-bishop1",
            {
                1: {"piece": "B"},
                3: {"label": "2"},
                5: {"label": "3"},
                6: {"piece": "Q"},
                7: {"label": "4"},
            },
            f"Step 4 — d12 = 9 → {subtract_roll_expr(9, 4, 4)} → Bishop on dark 1",
        ),
        (
            "step-05-light-labels",
            {
                1: {"piece": "B"},
                2: {"label": "1"},
                4: {"label": "2"},
                6: {"piece": "Q"},
                8: {"label": "3"},
            },
            "Step 5 — label empty light squares 1–3",
        ),
        (
            "step-06-bishop2",
            {
                1: {"piece": "B"},
                2: {"label": "1"},
                4: {"label": "2"},
                6: {"piece": "Q"},
                8: {"piece": "B"},
            },
            f"Step 6 — d12 = 9 → {subtract_roll_expr(9, 3, 3)} → Bishop on light 3",
        ),
        (
            "step-07-five-labels",
            {
                1: {"piece": "B"},
                2: {"label": "1"},
                3: {"label": "2"},
                4: {"label": "3"},
                5: {"label": "4"},
                6: {"piece": "Q"},
                7: {"label": "5"},
                8: {"piece": "B"},
            },
            "Step 7 — label five empty squares 1–5",
        ),
        (
            "step-08-knight1",
            {
                1: {"piece": "B"},
                2: {"piece": "N"},
                3: {"label": "2"},
                4: {"label": "3"},
                5: {"label": "4"},
                6: {"piece": "Q"},
                7: {"label": "5"},
                8: {"piece": "B"},
            },
            f"Step 8 — d20 = 16 → {subtract_roll_expr(16, 5, 5)} → Knight on 1",
        ),
        (
            "step-09-four-labels",
            {
                1: {"piece": "B"},
                2: {"piece": "N"},
                3: {"label": "1"},
                4: {"label": "2"},
                5: {"label": "3"},
                6: {"piece": "Q"},
                7: {"label": "4"},
                8: {"piece": "B"},
            },
            "Step 9 — label four empty squares 1–4",
        ),
        (
            "step-10-knight2",
            {
                1: {"piece": "B"},
                2: {"piece": "N"},
                3: {"label": "1"},
                4: {"label": "2"},
                5: {"label": "3"},
                6: {"piece": "Q"},
                7: {"piece": "N"},
                8: {"piece": "B"},
            },
            f"Step 10 — d20 = 16 → {subtract_roll_expr(16, 4, 4)} → Knight on 4",
        ),
        (
            "step-11-final",
            {
                1: {"piece": "B"},
                2: {"piece": "N"},
                3: {"piece": "R"},
                4: {"piece": "K"},
                5: {"piece": "R"},
                6: {"piece": "Q"},
                7: {"piece": "N"},
                8: {"piece": "B"},
            },
            "Step 11 — K on 2, R on 1 and 3",
        ),
    ]

    for stem, state, caption in steps:
        write_step(
            OUT_DIR / f"{stem}.svg",
            WIKI_DIR / f"{stem}.wiki",
            rank1_from_state(state),
            caption,
        )

    print(f"Wrote {len(steps)} diagrams to {OUT_DIR}")
    print(f"Wikitext sources: {WIKI_DIR}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        print(
            "Diagrams need network access to Wikipedia/Commons. "
            "See docs/FISCHER_RANDOM_960.md.",
            file=sys.stderr,
        )
        raise SystemExit(1) from exc
