#!/usr/bin/env python3
"""Export white chess piece glyphs as SVG via chessfss (skaknew board font)."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
EXPORT_DIR = REPO / "docs" / "fischer960" / "export"
PIECES_DIR = REPO / "docs" / "fischer960" / "pieces"

PIECE_FILL = "#ffffff"
PIECE_STROKE = "#2d2d2d"
PIECE_STROKE_WIDTH = "0.65"

# chessfss white pieces on a light square (rank-1 setup from White's perspective)
PIECES = {
    "king": "WhiteKingOnWhite",
    "queen": "WhiteQueenOnWhite",
    "rook": "WhiteRookOnWhite",
    "bishop": "WhiteBishopOnWhite",
    "knight": "WhiteKnightOnWhite",
}

TEX_TEMPLATE = r"""
\documentclass[border=2pt]{{standalone}}
\usepackage{{xcolor}}
\usepackage{{chessfss}}
\setboardfontcolors{{whitepiece=white,blackpiece=black}}
\begin{{document}}
{{\boardfont\fontsize{{{size}}}{{{size}}}\selectfont \{cmd}}}
\end{{document}}
"""

_PIECE_G_RE = re.compile(
    r'<g fill="rgb\((?:0%|100%), (?:0%|100%), (?:0%|100%)\)" fill-opacity="1">'
)


def run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def style_piece_svg(raw: str) -> str:
    """White fill + dark outline so pieces read on light and dark squares."""
    styled = _PIECE_G_RE.sub(
        f'<g fill="{PIECE_FILL}" stroke="{PIECE_STROKE}" '
        f'stroke-width="{PIECE_STROKE_WIDTH}">',
        raw,
        count=1,
    )
    return styled


def export_piece(name: str, cmd: str, size: int = 80) -> Path:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    PIECES_DIR.mkdir(parents=True, exist_ok=True)
    tex_name = f"piece-{name}.tex"
    tex_path = EXPORT_DIR / tex_name
    tex_path.write_text(
        TEX_TEMPLATE.format(size=size, cmd=cmd),
        encoding="utf-8",
    )
    run(
        [
            "pdflatex",
            "-halt-on-error",
            "-interaction=nonstopmode",
            tex_name,
        ],
        EXPORT_DIR,
    )
    pdf = EXPORT_DIR / f"piece-{name}.pdf"
    svg_path = PIECES_DIR / f"{name}.svg"
    cairo_base = EXPORT_DIR / f"piece-{name}-cairo"
    run(["pdftocairo", "-svg", str(pdf), str(cairo_base)], EXPORT_DIR)
    generated = Path(f"{cairo_base}.svg")
    if not generated.is_file():
        generated = Path(str(cairo_base))
    if not generated.is_file():
        raise FileNotFoundError(f"SVG not created for {name}")
    svg_path.write_text(
        style_piece_svg(generated.read_text(encoding="utf-8")),
        encoding="utf-8",
    )
    if generated != svg_path:
        generated.unlink(missing_ok=True)
    stale = PIECES_DIR / name
    if stale.is_file() and stale != svg_path:
        stale.unlink()
    return svg_path


def main() -> int:
    for name, cmd in PIECES.items():
        path = export_piece(name, cmd)
        print(f"Wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
