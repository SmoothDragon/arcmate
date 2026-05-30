# Scripts

## Python environment (uv)

This repo uses **[uv](https://docs.astral.sh/uv/)** with a root **`.venv`** and [`pyproject.toml`](../pyproject.toml). Card builds (`make`) still use system `python3` + LaTeX only.

### One-time setup

**1. Install uv** (per machine):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# ensure ~/.local/bin is on your PATH
```

**2. Project + Google credentials** (from repo root):

```bash
cd /path/to/arcmate
make setup          # or: ./scripts/setup_env.sh  →  uv sync
export GOOGLE_APPLICATION_CREDENTIALS="$PWD/scripts/secrets/service-account.json"
```

**3. Google Cloud** (for Sheets sync):

- Enable **Google Sheets API** and **Google Drive API**.
- Create a **service account** JSON key → `scripts/secrets/service-account.json` (gitignored).
- Share the [ChessRuleCards spreadsheet](https://docs.google.com/spreadsheets/d/1FEswgLlyckdUdkqBpFjGnMcEMd2lOh_IVsh94GkxTQg/edit) with the service account as **Editor** (not Viewer).

```bash
uv run python scripts/sync_json_to_sheet.py --show-account
```

Copy the printed email into **Share** on the spreadsheet. For this repo’s key that is:

`arcmate@warm-utility-242922.iam.gserviceaccount.com`

(If you use a different JSON key, run `--show-account` again — the email must match the key file.)

### Day to day

```bash
cd /path/to/arcmate
export GOOGLE_APPLICATION_CREDENTIALS="$PWD/scripts/secrets/service-account.json"

uv run python scripts/sync_json_to_sheet.py --dry-run
make sync-sheet      # same as uv run python scripts/sync_json_to_sheet.py
make               # PDF from arcmate.json (no uv needed for tex.py)
```

After editing `arcmate.json`:

```bash
make sync-sheet && make
```

### Files

| File | Role |
|------|------|
| [`pyproject.toml`](../pyproject.toml) | Dependencies (`gspread`, `google-auth`) |
| [`uv.lock`](../uv.lock) | Pinned versions — commit to git |
| [`.python-version`](../.python-version) | Python 3.12 for `uv` |
| `scripts/requirements-sheets.txt` | Legacy reference only; use `uv sync` |

### Environment variables

| Variable | Default |
|----------|---------|
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to service account JSON (required for sync) |
| `ARCMATE_SPREADSHEET_ID` | `1FEswgLlyckdUdkqBpFjGnMcEMd2lOh_IVsh94GkxTQg` |
| `ARCMATE_SHEET_TAB` | `arcmate_json` |

---

## `sync_json_to_sheet.py` — JSON → Google Sheets

Pushes [`arcmate.json`](../arcmate.json) (`text_cards` + `reference_cards`) to worksheet **`arcmate_json`**. **JSON → Sheet** (overwrites that tab).

### Columns written

| Column | Source |
|--------|--------|
| `canonical_id` | snake_case from `caption` |
| `card_type` | `text_card` or `reference_card` |
| `slot` | `R1` / `R2` for reference cards |
| `caption`, `description`, `origin`, `genre`, `quote`, `symbol`, `bottomcaption` | JSON |
| `json_index` | Index in array |
| `synced_at` | UTC time of push |

Other spreadsheet tabs (playtest scores, Origins 25 picks) are edited manually; this tab stays a mirror of JSON.

### Troubleshooting

| Error | Fix |
|-------|-----|
| `uv: command not found` | Install uv; add `~/.local/bin` to PATH |
| `Missing dependencies` | `uv sync` |
| `[403] The caller does not have permission` | **Share** the spreadsheet with the `--show-account` email as **Editor**; enable Sheets + Drive APIs in the GCP project |
| `SpreadsheetNotFound` | Wrong spreadsheet ID or no share |
