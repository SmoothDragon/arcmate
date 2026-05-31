#!/usr/bin/env python3
"""Build and render {{Chess diagram}} (Module:Chessboard / Commons Staunton pieces)."""

from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

USER_AGENT = "ArcMateFischer960/1.0 (https://github.com/tom/arcmate; educational)"
WIKI_API = "https://en.wikipedia.org/w/api.php"
COMMONS_BASE = "https://upload.wikimedia.org/wikipedia/commons"
# Wikipedia Chessboard480.svg colors
BOARD_LIGHT = "#ffce9e"
BOARD_DARK = "#d18b47"


def build_chess_diagram_wikitext(
    rank1: dict[int, str],
    header: str = "",
    footer: str = "",
    *,
    size: int = 32,
    numbers: str = "neither",
    letters: str = "bottom",
    align: str = "",
) -> str:
    """rank1: file 1–8 (a–h) → two-char square codes (ql, x1, bl, …)."""
    def row(files: dict[int, str]) -> str:
        cells = [files.get(f, "  ") for f in range(1, 9)]
        return "|" + "|".join(cells) + "|"

    rank_rows = [row({}) for _ in range(7)] + [row(rank1)]
    lines = [
        "{{Chess diagram",
        f"| {align}".rstrip(),
        f"| {header}",
        f"| size={size}",
        f"| numbers={numbers}",
        f"| letters={letters}",
        *rank_rows,
    ]
    if footer:
        lines.append(f"| {footer}")
    lines.append("}}")
    return "\n".join(lines)


def code_to_filename(code: str) -> str | None:
    code = code.strip()
    if not code:
        return None
    return f"Chess_{code}t45.svg"


def resolve_commons_url(filename: str, cache_dir: Path) -> str:
    manifest = cache_dir / "urls.json"
    urls: dict[str, str] = {}
    if manifest.is_file():
        urls = json.loads(manifest.read_text(encoding="utf-8"))
    if filename in urls:
        return urls[filename]
    params = urllib.parse.urlencode(
        {
            "action": "query",
            "format": "json",
            "titles": f"File:{filename}",
            "prop": "imageinfo",
            "iiprop": "url",
        }
    )
    req = urllib.request.Request(
        f"{WIKI_API}?{params}",
        headers={"User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    pages = data["query"]["pages"]
    page = next(iter(pages.values()))
    url = page["imageinfo"][0]["url"]
    urls[filename] = url
    manifest.write_text(json.dumps(urls, indent=2), encoding="utf-8")
    return url


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.is_file():
        return
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        dest.write_bytes(resp.read())


def board_rank1_squares_svg(sq: int) -> str:
    """Single rank (White's rank 1): a1 dark … h1 light, Wikipedia colors."""
    rects = []
    for file in range(8):
        file_num = file + 1
        light = file_num % 2 == 0
        fill = BOARD_LIGHT if light else BOARD_DARK
        rects.append(
            f'<rect x="{file * sq}" y="0" width="{sq}" height="{sq}" fill="{fill}"/>'
        )
    return "\n".join(rects)


def piece_position_rank1(file_num: int, size: int) -> tuple[int, int]:
    left = (file_num - 1) * size
    return left, 0


def render_diagram_svg(
    rank1: dict[int, str],
    out_path: Path,
    *,
    cache_dir: Path,
    size: int = 32,
    caption: str = "",
) -> None:
    """Render White's rank 1 only (8 files), Commons Staunton pieces inlined."""
    rank_h = size
    rank_w = 8 * size
    label_h = 18
    cap_h = 14 if caption else 0
    total_h = rank_h + label_h + cap_h
    total_w = rank_w

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="{total_w}" height="{total_h}" viewBox="0 0 {total_w} {total_h}">',
        board_rank1_squares_svg(size),
    ]

    for i, file_num in enumerate(range(1, 9)):
        code = rank1.get(file_num, "  ").strip()
        if not code:
            continue
        filename = code_to_filename(code)
        if not filename:
            continue
        local = cache_dir / filename
        if not local.is_file():
            url = resolve_commons_url(filename, cache_dir)
            download(url, local)
        inner = local.read_text(encoding="utf-8")
        inner_m = re.search(r"<svg[^>]*>(.*)</svg>", inner, re.DOTALL | re.I)
        if not inner_m:
            continue
        body = inner_m.group(1).strip()
        pid = f"wp{i}"
        body = re.sub(r'\bid="([^"]+)"', lambda m: f'id="{pid}-{m.group(1)}"', body)
        body = re.sub(
            r'(?:xlink:)?href="#([^"]+)"',
            lambda m: f'xlink:href="#{pid}-{m.group(1)}"',
            body,
        )
        left, top = piece_position_rank1(file_num, size)
        parts.append(
            f'<svg x="{left}" y="{top}" width="{size}" height="{size}" '
            f'viewBox="0 0 45 45" overflow="visible">{body}</svg>'
        )

    letters = "abcdefgh"
    for i, letter in enumerate(letters):
        cx = i * size + size / 2
        parts.append(
            f'<text x="{cx:.1f}" y="{rank_h + 14}" text-anchor="middle" '
            f'font-family="DejaVu Sans,sans-serif" font-size="13" fill="#333">{letter}</text>'
        )

    if caption:
        parts.append(
            f'<text x="{total_w/2:.1f}" y="{total_h - 2}" text-anchor="middle" '
            f'font-family="DejaVu Sans,sans-serif" font-size="11" fill="#555">{_esc(caption)}</text>'
        )

    parts.append("</svg>\n")
    out_path.write_text("\n".join(parts), encoding="utf-8")


def _esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )
