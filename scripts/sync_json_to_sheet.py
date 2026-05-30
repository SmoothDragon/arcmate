#!/usr/bin/env python3
"""
Push card text from arcmate.json to a Google Spreadsheet tab.

JSON is the source of truth; this script overwrites the target worksheet
so the sheet always matches the file used to build cards (arcmate.tex.py).

Setup: see scripts/README.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Default spreadsheet: ChessRuleCards (group catalog)
DEFAULT_SPREADSHEET_ID = "1FEswgLlyckdUdkqBpFjGnMcEMd2lOh_IVsh94GkxTQg"
DEFAULT_WORKSHEET_TITLE = "arcmate_json"

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = REPO_ROOT / "arcmate.json"
DEFAULT_CREDENTIALS = REPO_ROOT / "scripts/secrets/service-account.json"
SHEET_SHARE_URL = (
    "https://docs.google.com/spreadsheets/d/1FEswgLlyckdUdkqBpFjGnMcEMd2lOh_IVsh94GkxTQg/edit"
)

HEADERS = [
    "canonical_id",
    "card_type",
    "slot",
    "caption",
    "description",
    "origin",
    "genre",
    "quote",
    "symbol",
    "bottomcaption",
    "json_index",
    "synced_at",
]

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def caption_to_canonical_id(caption: str) -> str:
    """Match docs/CARD_LIST.md style ids (snake_case from caption)."""
    s = caption.lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


def load_cards(json_path: Path) -> list[dict]:
    with json_path.open(encoding="utf-8") as f:
        data = json.load(f)

    rows: list[dict] = []
    synced_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    for i, card in enumerate(data.get("text_cards", [])):
        rows.append(
            {
                "canonical_id": caption_to_canonical_id(card.get("caption", "")),
                "card_type": "text_card",
                "slot": "",
                "caption": card.get("caption", ""),
                "description": card.get("description", ""),
                "origin": card.get("origin", ""),
                "genre": card.get("genre", ""),
                "quote": card.get("quote", ""),
                "symbol": card.get("symbol", ""),
                "bottomcaption": card.get("bottomcaption", ""),
                "json_index": i,
                "synced_at": synced_at,
            }
        )

    for i, card in enumerate(data.get("reference_cards", [])):
        rows.append(
            {
                "canonical_id": caption_to_canonical_id(card.get("caption", "")),
                "card_type": "reference_card",
                "slot": card.get("slot", ""),
                "caption": card.get("caption", ""),
                "description": card.get("description", ""),
                "origin": card.get("origin", ""),
                "genre": card.get("genre", ""),
                "quote": card.get("quote", ""),
                "symbol": card.get("symbol", ""),
                "bottomcaption": card.get("bottomcaption", ""),
                "json_index": i,
                "synced_at": synced_at,
            }
        )

    return rows


def rows_to_values(rows: list[dict]) -> list[list[str]]:
    table = [HEADERS]
    for row in rows:
        table.append([str(row.get(h, "")) for h in HEADERS])
    return table


def service_account_email(credentials_path: Path) -> str:
    with credentials_path.open(encoding="utf-8") as f:
        return json.load(f)["client_email"]


def get_gspread_client(credentials_path: Path):
    try:
        import gspread
        from google.oauth2.service_account import Credentials
    except ImportError as e:
        print(
            "Missing dependencies. Install with:\n"
            "  uv sync\n"
            "  uv run python scripts/sync_json_to_sheet.py ...",
            file=sys.stderr,
        )
        raise SystemExit(1) from e

    creds = Credentials.from_service_account_file(
        str(credentials_path), scopes=SCOPES
    )
    return gspread.authorize(creds)


def ensure_worksheet(spreadsheet, title: str, min_rows: int):
    import gspread

    try:
        return spreadsheet.worksheet(title)
    except gspread.exceptions.WorksheetNotFound:
        return spreadsheet.add_worksheet(
            title=title, rows=max(min_rows, 100), cols=len(HEADERS)
        )


def explain_permission_error(
    exc: Exception,
    credentials_path: Path,
    spreadsheet_id: str,
) -> None:
    email = service_account_email(credentials_path)
    print(
        f"\nGoogle API permission error ({exc}).\n\n"
        "Most often the spreadsheet is not shared with the service account.\n\n"
        f"  1. Open: {SHEET_SHARE_URL}\n"
        "  2. Click Share\n"
        f"  3. Add this email as Editor:\n\n"
        f"       {email}\n\n"
        "  4. Re-run: make sync-sheet\n\n"
        "Also verify in Google Cloud project for this key:\n"
        "  - Google Sheets API enabled\n"
        "  - Google Drive API enabled\n",
        file=sys.stderr,
    )


def push_to_sheet(
    values: list[list[str]],
    spreadsheet_id: str,
    worksheet_title: str,
    credentials_path: Path,
) -> None:
    import gspread

    client = get_gspread_client(credentials_path)
    try:
        spreadsheet = client.open_by_key(spreadsheet_id)
    except gspread.exceptions.APIError as exc:
        if getattr(exc, "response", None) and exc.response.status_code == 403:
            explain_permission_error(exc, credentials_path, spreadsheet_id)
            raise SystemExit(1) from exc
        raise
    try:
        worksheet = ensure_worksheet(spreadsheet, worksheet_title, len(values))
    except gspread.exceptions.APIError as exc:
        if getattr(exc, "response", None) and exc.response.status_code == 403:
            explain_permission_error(exc, credentials_path, spreadsheet_id)
            raise SystemExit(1) from exc
        raise

    worksheet.clear()
    worksheet.update(values, value_input_option="RAW")

    # Freeze header row for scrolling
    try:
        spreadsheet.batch_update(
            {
                "requests": [
                    {
                        "updateSheetProperties": {
                            "properties": {
                                "sheetId": worksheet.id,
                                "gridProperties": {"frozenRowCount": 1},
                            },
                            "fields": "gridProperties.frozenRowCount",
                        }
                    }
                ]
            }
        )
    except Exception:
        pass  # non-fatal


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync arcmate.json card text to a Google Sheet tab."
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=DEFAULT_JSON,
        help=f"Path to arcmate.json (default: {DEFAULT_JSON})",
    )
    parser.add_argument(
        "--spreadsheet-id",
        default=None,
        help=f"Google spreadsheet ID (default: env ARCMATE_SPREADSHEET_ID or {DEFAULT_SPREADSHEET_ID})",
    )
    parser.add_argument(
        "--worksheet",
        default=None,
        help=f"Worksheet tab title (default: env ARCMATE_SHEET_TAB or {DEFAULT_WORKSHEET_TITLE})",
    )
    parser.add_argument(
        "--credentials",
        type=Path,
        default=None,
        help="Service account JSON key (default: env GOOGLE_APPLICATION_CREDENTIALS)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print row count and sample; do not call Google API",
    )
    parser.add_argument(
        "--show-account",
        action="store_true",
        help="Print service account email to add in Google Sheets Share dialog",
    )
    args = parser.parse_args()

    import os

    spreadsheet_id = (
        args.spreadsheet_id
        or os.environ.get("ARCMATE_SPREADSHEET_ID")
        or DEFAULT_SPREADSHEET_ID
    )
    worksheet_title = (
        args.worksheet
        or os.environ.get("ARCMATE_SHEET_TAB")
        or DEFAULT_WORKSHEET_TITLE
    )

    creds_path = args.credentials
    if creds_path is None:
        env_creds = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        if env_creds:
            creds_path = Path(env_creds)
        elif DEFAULT_CREDENTIALS.is_file():
            creds_path = DEFAULT_CREDENTIALS

    if args.show_account:
        if creds_path is None or not creds_path.is_file():
            print("No credentials file found.", file=sys.stderr)
            return 1
        print(service_account_email(creds_path))
        print(f"\nShare the sheet with that address (Editor):\n  {SHEET_SHARE_URL}")
        return 0

    if not args.json.is_file():
        print(f"JSON not found: {args.json}", file=sys.stderr)
        return 1

    rows = load_cards(args.json)
    values = rows_to_values(rows)

    print(f"Loaded {len(rows)} cards from {args.json}")
    print(f"Target: spreadsheet={spreadsheet_id} worksheet={worksheet_title!r}")

    if args.dry_run:
        print(f"Would write {len(values)} rows (1 header + {len(rows)} cards)")
        if rows:
            print("Sample row:", dict(zip(HEADERS, values[1])))
        return 0

    if creds_path is None or not creds_path.is_file():
        print(
            "Credentials required. Either:\n"
            "  export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json\n"
            "  scripts/sync_json_to_sheet.py --credentials /path/to/key.json\n"
            "See scripts/README.md for setup.",
            file=sys.stderr,
        )
        return 1

    try:
        push_to_sheet(values, spreadsheet_id, worksheet_title, creds_path)
    except SystemExit:
        raise
    except Exception as exc:
        import gspread

        if isinstance(exc, gspread.exceptions.APIError) and getattr(
            exc.response, "status_code", None
        ) == 403:
            explain_permission_error(exc, creds_path, spreadsheet_id)
            return 1
        raise

    print(f"Synced {len(rows)} cards to worksheet {worksheet_title!r}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
