# ArcMate — Comic-Con launch plan

Prototype goal: a **playable, teachable, professionally printed** deck of chess rule-modifying cards for **San Diego Comic-Con** (late July). This document tracks milestones, decisions, and how the repo, spreadsheet, and printer fit together.

**Related links**

| Resource | URL |
|----------|-----|
| Card catalog (group spreadsheet) | [ChessRuleCards Google Sheet](https://docs.google.com/spreadsheets/d/1FEswgLlyckdUdkqBpFjGnMcEMd2lOh_IVsh94GkxTQg/edit?usp=sharing) |
| Parent card corpus | [SmoothDragon/ChessRuleCards](https://github.com/SmoothDragon/ChessRuleCards) (subset becomes ArcMate) |
| Print vendor (target) | [Your Playing Cards](https://yourplayingcards.com/) — poker-sized custom decks, backs-only or full-face |
| Comic-Con submission notes | [`COMIC_CON_SUBMISSION.md`](COMIC_CON_SUBMISSION.md) |
| Printable source of truth (today) | [`arcmate.json`](arcmate.json) → [`arcmate.tex.py`](arcmate.tex.py) → [`Makefile`](Makefile) → `arcmate.pdf` |

---

## 1. Product definition

### SDCC goal: **ArcMate: Origins** (27 faces)

| Slot | Count | Purpose |
|------|-------|---------|
| **Rule cards** | **25** | Chess rule modifiers (curated from pool; see [PLAYTEST.md](docs/PLAYTEST.md)) |
| **Reference cards** | **2** | Non-random “utility” faces — see below |
| **Total per Origins deck** | **27** | 25 rules + R1 + R2 (reference cards not shuffled into the rule pile) |
| **Expansion** | — | Post-SDCC; **not** in this print |

**Play modes:** Standard chess, **Fischer Random 960** (dice setup on reference card), and bughouse for demos ([`COMIC_CON_SUBMISSION.md`](COMIC_CON_SUBMISSION.md)).

### Print plan: **one 54-card order = two Origins decks**

Use the manufacturer’s standard **54-card poker deck** SKU ([Your Playing Cards](https://yourplayingcards.com/) and similar vendors). **Do not** treat 54 as “one deck with leftovers” — it is **two complete copies** of the same 27-face product:

```
┌─────────────────────────────────────────────────────────────┐
│  54-card print (single order, one box SKU)                  │
├──────────────────────────┬──────────────────────────────────┤
│  Cards 1–27              │  Cards 28–54                   │
│  ArcMate: Origins #1     │  ArcMate: Origins #2 (duplicate)│
│  25 rule + R1 + R2       │  same 27 faces again             │
└──────────────────────────┴──────────────────────────────────┘
```

| Metric | Value |
|--------|--------|
| **Unique faces to design** | **27** (25 rule + 2 reference) |
| **Faces per print upload** | **54** (each unique face assigned twice in deck builder) |
| **Playable decks per print unit** | **2** |
| **Card order** | Lock sort order (e.g. alphabetical or playtest tier); **same order** in both halves |

**Why:** Matches the cheapest poker-deck price point (~$8.99/deck tier at volume) while SDCC needs **≥2 tables** without paying for two separate minimum orders.

**At Comic-Con:** One manufacturer unit → split into two tuck piles (Origins #1 / #2). Order **extra** 54-card units if you want spares (see §8).

### The 2 reference card slots

Reserved in [`arcmate.json`](arcmate.json) as `reference_cards` (not dealt as random rules). Pick final art/layout in W2; content draft:

| Slot | Working title | Purpose |
|------|---------------|---------|
| **R1** | **ArcMate rules** | Table reference: deal order, no-check win, compound turns (“done”), pawn limits, `+` draws — condense [QUICKREF.md](QUICKREF.md) |
| **R2** | **Fischer Random 960** | Dice algorithm + example **(6, 9, 16)** — [docs/FISCHER_RANDOM_960.md](docs/FISCHER_RANDOM_960.md) with step diagrams |

**Alternates** (swap in only if group prefers): title/branding card; bughouse one-pager; “how to teach in 3 minutes.” Keep **two** slots fixed so rule count stays **25**.

### Expansion (post-SDCC)

**ArcMate: _[name TBD]_** — separate future deck; not part of the Origins 27. Revisit after SDCC feedback.

---

## 2. Timeline (working backward from late July)

Assume Comic-Con **~July 23–26, 2026**. Adjust dates when booth days are confirmed.

| Week (approx.) | Dates | Milestone |
|----------------|-------|-----------|
| **W0** | Now | Plan agreed; **25 + 2** Origins structure; spreadsheet columns finalized |
| **W1** | Early June | **Glossary + rule skeleton**; `reference_cards` in JSON; poker export spec locked |
| **W2** | Mid June | **Final 25 rule cards** chosen; reference card text locked; cover art v1 in repo |
| **W3** | Late June | **Playtest round 1** (local + async); spreadsheet scores filled; ambiguous cards rewritten |
| **W4** | Early July | **Layout pass** for poker size; export test images; **place print order** (allow 1–2 weeks production + ship) |
| **W5** | Mid July | **Playtest round 2** on printed proof or high-res PDF; **rulebook v1** PDF for table |
| **W6** | Late July | **SDCC kit**: decks, boards/clocks, one-page teach sheet, signup/feedback (optional) |

**Hard deadline:** Print order **no later than ~July 7** if turnaround is ~10–14 days plus shipping (verify with [Your Playing Cards](https://yourplayingcards.com/) turnaround page before committing).

---

## 3. Card data: spreadsheet ↔ `arcmate.json` ↔ PDF

### Current pipeline

```
arcmate.json  →  arcmate.tex.py (buildMagicTeX)  →  arcmate.tex  →  Makefile  →  arcmate.pdf
```

- **33** rule candidates in `text_cards` today → cut to **25** for Origins; **2** in `reference_cards`.
- Layout uses **Magic-sized** dimensions in `Magic_TikZ_card` (~63×88 mm). Poker is **2.5″×3.5″** (~63.5×88.9 mm) — close, but **export for the vendor must be per-card raster/PDF at 300 DPI**, not only a multi-card letter sheet.

### Spreadsheet role (recommended)

Use the [Google Sheet](https://docs.google.com/spreadsheets/d/1FEswgLlyckdUdkqBpFjGnMcEMd2lOh_IVsh94GkxTQg/edit?usp=sharing) for **workflow and curation**, not duplicate full card text long-term.

| Column group | Purpose | Lives in |
|--------------|---------|----------|
| **Identity** | Canonical name, ChessRuleCards link, `caption` match | Sheet + JSON (`caption`) |
| **Selection** | In Origins 25? Cut / expansion-later | Sheet (source of truth) |
| **Quality rubric** | Dynamic change, No legality check, Avoid 1v1 draws, Intuitive, No tokens (existing headers) | Sheet |
| **Playtest** | Fun, clarity, combo risk, teach time | Sheet |
| **Print** | Face file name, slot (rule vs R1/R2), last exported hash | Sheet or CI |
| **Rules text** | `description`, `symbol`, `origin`, `genre`, `quote` | **`arcmate.json`** (source of truth for rendering) |

**Principle:** One source of truth per field type — avoid editing the same sentence in two places.

### Sync strategy (pick one; recommended: **hybrid**)

| Approach | Pros | Cons |
|----------|------|------|
| **A. JSON only** | Simple repo workflow; PDF always in sync | Sheet becomes stale for playtest notes |
| **B. Sheet only** | Great for non-devs | Harder to diff; weak LaTeX integration |
| **C. Hybrid (recommended)** | Devs edit JSON; group edits sheet metadata; script merges | Needs a small import/export script |

**Hybrid workflow**

1. Group edits **inclusion, deck, scores, notes** in the Sheet.
2. Designers edit **card text** in `arcmate.json` (or generated from Sheet export — see below).
3. **JSON → Sheet:** [`scripts/sync_json_to_sheet.py`](scripts/sync_json_to_sheet.py) → tab **`arcmate_json`** via `make sync-sheet` ([uv setup](scripts/README.md)). Run after editing `arcmate.json`.
4. Future: Sheet → JSON import for metadata only (`origins_include`, playtest scores) — never silent overwrite of `description`.

**Name alignment:** Sheet uses names like “All Passant”; JSON uses `ALL PASSANT`. Maintain a **`canonical_id`** column (snake_case) in both places.

---

## 4. Physical production ([Your Playing Cards](https://yourplayingcards.com/))

Aligns with [§1 print plan](#print-plan-one-54-card-order--two-origins-decks): **54-card poker SKU = two ArcMate: Origins decks**.

- **Poker size** (2.5″ × 3.5″), fully custom faces and one **Origins** back.
- **27 unique designs** → **54 slots** in the deck builder (each face twice).
- Face spec: typically **750×1050 px @ 300 DPI** + bleed per vendor template.

### Engineering tasks

| Task | Owner | Notes |
|------|-------|-------|
| Add `Poker_TikZ_card` / `buildPokerTeX` | Dev | ~6.35×8.89 cm; increase safe margins (3–5 mm) for trim |
| Per-card PNG/PDF export | Dev | **27** files; duplicate to **54-slot** upload manifest |
| `origins_deck_order` | Dev | Locked card positions 1–27 (repeated 28–54) |
| Bleed / CMYK | Design | Proof one 54-card unit (= 2 decks) before bulk |
| Proof order | Group | 1×54 unit minimum |

### MTG → poker migration note

Dimensions are **almost the same** as Magic (63×88 mm). The main work is **54 upload slots** (27×2) and typography in the safe zone, not a full redesign.

---

## 5. Deck composition & card selection

### Pool

- Start from **[ChessRuleCards](https://github.com/SmoothDragon/ChessRuleCards)** (superset).
- Current **`arcmate.json`** is an early subset (32 cards); several names differ from the Sheet (e.g. “Attack swap” vs `CAPTURE SWAP`).

### Selection criteria (use Sheet rubric + playtest)

| Criterion | Target for SDCC |
|-----------|-------------------|
| **Playtest score** | Prefer **4–5/5** from [docs/PLAYTEST.md](docs/PLAYTEST.md); cut **3/5** “degenerate to chess” (e.g. Teleporter) |
| **Teachable in <2 min** | Prefer cards that need no extra tokens |
| **Composable** | Cards stack via “current rules” model (README master rules) |
| **Bughouse-safe** | Avoid rules that break two-board timing unless tested |
| **No adjudication hell** | Deprioritize “No legality check” = fail in Sheet |
| **1v1 stall** | Deprioritize rules that increase draws in single-board chess |
| **Balance** | Mix `origin` (C/I/F), `genre` (+, T, diff, -) across **25** rules; note **Cylinder** White edge |

**Adam & Jay-C Tier A (5/5) for Origins:** Ghost, Move twice, Insane cylinder, Micro-manager, Cylinder. **Tier B (4/5):** Capture twice, War and Peace, Summoner, Precocious pawns, Possession. **Tier C:** Teleporter → expansion or cut.

### Playtest protocol

1. **Single-card smoke test** — deal 1 card, play one game, rate clarity 1–5.
2. **Two-card stack test** — deal 2 (order matters); note conflicts in Sheet “combo notes”.
3. **Bughouse session** — 4 players, 5+5 clocks, record broken rules.
4. **Cut list** — bottom quartile by (fun + clarity) unless strategically kept for expansion identity.

### Deliverable

- [docs/PLAYTEST.md](docs/PLAYTEST.md) — session notes + inclusion tiers (started).
- [docs/CARD_LIST.md](docs/CARD_LIST.md) + Sheet tab: **25** rule IDs + **R1/R2** locked.

---

## 6. Rules, terminology, ambiguity

### Documents

| Doc | Purpose |
|-----|---------|
| [`GLOSSARY.md`](GLOSSARY.md) | Definitions from [`arcmate.txt`](arcmate.txt); style rules (no take/attack) |
| [`RULEBOOK.md`](RULEBOOK.md) | Full rules draft v0.1; Fischer Random; bughouse; open questions |
| [`QUICKREF.md`](QUICKREF.md) | One-page teach sheet |
| [`docs/CARD_LIST.md`](docs/CARD_LIST.md) | Per-card status vs `arcmate.txt`; JSON fix queue |

### Standardize terminology (decisions)

| Term | Current usage | Proposed standard |
|------|---------------|-------------------|
| Move / capture / act | Mixed on cards | **Move** = relocation; **capture** = removal by rule; **act** = any legal turn action including special |
| “X” / piece classes | `\KI`, `\NoKing`, etc. | Glossary table mapping macros → English |
| Card name | Sheet vs JSON mismatches | One **canonical_id** + display **caption** |
| “Draw extra card” | README: first `+` only | Rulebook must state clearly for demos |

### Ambiguity pass (before print)

- [x] **Win condition:** no check; king presence at end of turn ([PLAYTEST.md](docs/PLAYTEST.md) → [RULEBOOK.md](RULEBOOK.md) v0.2).
- [ ] **Global pawn rules** on cards + rulebook (min rank, 10×10 → rank 9, summoner limits).
- [ ] **Ghost** interactions: castling, pawn capture, en passant.
- [ ] Every card: **trigger**, **duration**, **who chooses** targets.
- [ ] Rules that need **extra equipment** (10×10 board, cylinder diagram): include **setup diagram** on card or ban for Origins.
- [ ] **Compound turns:** “turn over” + Move Twice White move-1 ban on [QUICKREF.md](QUICKREF.md).

---

## 7. Art & branding

| Asset | Status | Notes |
|-------|--------|-------|
| **Card backs** | Needed | Origins back; ChatGPT drafts → repo `art/backs/` |
| **Box / tuck** | Vendor default | Window tuck often included; add logo sticker if needed |
| **Logo / wordmark** | TBD | ArcMate: Origins |
| **Table banner** | Optional | For SDCC visibility |
| **Rule icons** | In repo | `symbols.tex`, `graphics/` — verify legibility at poker size |

**Process:** Place approved art in repo; reference paths from JSON (`graphic` field pattern already partially supported in `Magic_TikZ_card`).

---

## 8. Comic-Con operations

From [`COMIC_CON_SUBMISSION.md`](COMIC_CON_SUBMISSION.md) — operational checklist:

| Item | Qty / note |
|------|------------|
| Printed decks | **1× 54-card print → 2 Origins decks**; add **2nd print unit** (4 decks) or **3rd** for spare if budget allows ([§1 print plan](#print-plan-one-54-card-order--two-origins-decks)) |
| Demo boards | Chess + bughouse (or dual demo board) |
| Clocks | 5+5 for advertised length |
| Laminated quick-ref | 4+ copies |
| **Teach script** | 60-second pitch + 3-minute teach |
| **Feedback** | QR → form or Sheet tab “SDCC feedback” |
| **Legal** | Repo licenses: GPL + CC-BY-NC-SA — confirm quotes on cards and NC use at con |

---

## 9. Repository task backlog

### P0 (before print order)

- [ ] Resize / export path for **poker** + **54-slot** vendor manifest (27 unique × 2)
- [ ] Finalize **Origins 25** from [PLAYTEST.md](docs/PLAYTEST.md) + untested passes; lock **R1/R2** reference text
- [x] `GLOSSARY.md` + `RULEBOOK.md` v0.2 + `QUICKREF.md` + `docs/CARD_LIST.md` + `docs/PLAYTEST.md`
- [x] Patch JSON: Summoner, Ten By Ten, Move Twice, War and Peace; add Possession
- [ ] Cut/move Teleporter; distinguish Possession vs Lend Me Your Horse
- [x] Spreadsheet ↔ JSON **export:** `scripts/sync_json_to_sheet.py` → tab `arcmate_json`
- [ ] Sheet → JSON metadata import (optional); agree hybrid workflow with group
- [ ] Cover art in repo; wire backs into print export
- [ ] Proof deck ordered

### P1 (before SDCC)

- [ ] Playtest round 2 on physical cards
- [ ] `QUICKREF` printed (laminated for table)
- [ ] Name expansion; update JSON metadata (`deck`: `origins` | `expansion`)
- [x] README points to PLAN, rulebook, glossary, card list, `arcmate.txt`

### P2 (nice to have)

- [ ] `graphic_cards` populated for heavy visual rules
- [ ] CI: `make` fails if JSON captions ≠ Sheet export
- [ ] Online rules page / repo wiki

---

## 10. Open decisions (resolve in W0–W1)

| # | Decision | Options | Recommendation |
|---|----------|---------|----------------|
| 1 | **Which 25 rules** | Ranked list in CARD_LIST + Sheet | Tier A/B playtest + cut Teleporter |
| 2 | **R1 vs R2 content** | Rules ref vs 960 dice (default) | As table above; alternates only if still 2 slots |
| 3 | **Print SKU** | **Resolved:** 54 = 2× Origins (27 unique faces × 2) | Confirm deck builder accepts duplicate mapping |
| 4 | **Quotes on cards** | Keep / shorten / remove | Shorten or drop for SDCC |
| 5 | **Sheet vs JSON authority** | Hybrid | Hybrid |
| 6 | **Primary demo mode** | Chess vs bughouse | Chess + 1 card; 960 via **R2** |
| 7 | **Print quantity** | | e.g. **2× 54-card units** → 4 decks for 2 tables + margin; 1 unit for proof |
| 8 | **ChessRuleCards licensing** | | Confirm derivative use |
| 9 | **Expansion** | Post-SDCC | Name TBD; not in Origins 27 |

---

## 11. Success criteria (SDCC)

- [ ] Stranger can play one **complete game in 15 minutes** after a 3-minute teach.
- [ ] No rule argument unresolved in >60 seconds (quick-ref covers 90% cases).
- [ ] Printed cards shuffle and read like commercial poker cards.
- [ ] Group can update card ratings in the Sheet during/after con without breaking the PDF build.
- [ ] Clear list of **v2 changes** (cut cards, wording, expansion name) captured before teardown.

---

## 12. Roles (fill in names)

| Area | Owner |
|------|-------|
| Spreadsheet / playtest coordination | |
| `arcmate.json` + LaTeX export | |
| Rulebook & glossary | |
| Art (backs, logo) | |
| Print order & vendor liaison | |
| SDCC booth / scheduling | |

---

*Last updated: 2026-05-30 (Origins = 25 + 2 reference; **54-card print = 2 decks**). Revise when booth dates and printer turnaround are confirmed.*
