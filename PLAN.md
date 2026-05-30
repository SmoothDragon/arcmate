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

### What we are shipping for SDCC

| Item | Target |
|------|--------|
| **Base game** | **ArcMate: Origins** — 27 rule cards |
| **Expansion** | **ArcMate: _[name TBD]_** — 27 rule cards |
| **Physical product** | One **54-card poker deck** (cheapest path on [Your Playing Cards](https://yourplayingcards.com/): standard poker size, custom backs; customize faces per card in their deck builder) |
| **Play modes** | Standard chess and **Fischer Random / bughouse** (per README and Comic-Con form) |
| **Demo format** | 10–15 min games; rules taught on-site ([`COMIC_CON_SUBMISSION.md`](COMIC_CON_SUBMISSION.md)) |

### What “54 cards” really means

Confirm with the printer how they count cards (52 + 2 jokers vs 54 distinct faces). Typical options:

| Slot | Suggested use | Decision needed |
|------|---------------|-----------------|
| 52 | Rule cards (26 Origins + 26 Expansion) | Or 27+27 and drop 2 slots |
| 2 | Jokers / “draw 2” / reference | Or rule-summary cards |
| **27 + 27** | Matches your split | **2 cards** must be non-rule (jokers, title card, quick-ref) **or** you print **56** and pay more — **decide by playtest week 2** |

**Recommendation:** Treat **52 faces as rules** (26 per box conceptually) and use **2 jokers** for “reshuffle / blank / ArcMate logo” so the printer’s 54-card SKU stays valid without wasting rule slots.

---

## 2. Timeline (working backward from late July)

Assume Comic-Con **~July 23–26, 2026**. Adjust dates when booth days are confirmed.

| Week (approx.) | Dates | Milestone |
|----------------|-------|-----------|
| **W0** | Now | This plan agreed; spreadsheet columns finalized; expansion name shortlist |
| **W1** | Early June | **Glossary + rule skeleton**; fix known data bugs in `arcmate.json`; poker export spec locked |
| **W2** | Mid June | **Card pool frozen** (candidates from ChessRuleCards); Origins vs Expansion assignment v1; cover art v1 in repo |
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

- **32** cards in `text_cards` today (not yet 27+27).
- Layout uses **Magic-sized** dimensions in `Magic_TikZ_card` (~63×88 mm). Poker is **2.5″×3.5″** (~63.5×88.9 mm) — close, but **export for the vendor must be per-card raster/PDF at 300 DPI**, not only a multi-card letter sheet.

### Spreadsheet role (recommended)

Use the [Google Sheet](https://docs.google.com/spreadsheets/d/1FEswgLlyckdUdkqBpFjGnMcEMd2lOh_IVsh94GkxTQg/edit?usp=sharing) for **workflow and curation**, not duplicate full card text long-term.

| Column group | Purpose | Lives in |
|--------------|---------|----------|
| **Identity** | Canonical name, ChessRuleCards link, `caption` match | Sheet + JSON (`caption`) |
| **Selection** | In SDCC deck? Origins / Expansion / cut | Sheet (source of truth) |
| **Quality rubric** | Dynamic change, No legality check, Avoid 1v1 draws, Intuitive, No tokens (existing headers) | Sheet |
| **Playtest** | Fun, clarity, combo risk, teach time | Sheet |
| **Print** | Face file name, back deck (Origins vs Expansion), last exported hash | Sheet or CI |
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
3. Add `scripts/sync_cards.py` (or Makefile target):
   - **Export:** JSON → CSV (`caption`, `description`, `origin`, `genre`, `deck`, `github_path`) for Sheet import / validation.
   - **Import:** Sheet CSV → update only allowed columns in JSON (`deck`, `include`, `notes`) — never silently overwrite `description` without review.
4. Optional: Google Apps Script on the Sheet to pull CSV from a **raw GitHub URL** on each release tag.

**Name alignment:** Sheet uses names like “All Passant”; JSON uses `ALL PASSANT`. Maintain a **`canonical_id`** column (snake_case) in both places.

---

## 4. Physical production ([Your Playing Cards](https://yourplayingcards.com/))

### Cheapest path (your direction)

- **Poker size** (2.5″ × 3.5″).
- **54-card deck** SKU.
- **Custom backs** per product line (Origins back vs Expansion back) may require **two separate 27-card orders** or one 54-card order with shared back — **get quote for both**; two 27-card runs might cost more than one 54-card run.
- **Faces:** “Fully custom” faces = upload **one image per card** (typical minimum **750×1050 px @ 300 DPI**, RGB/CMYK per their FAQ; use their template when the deck builder provides it).

### Engineering tasks

| Task | Owner | Notes |
|------|-------|-------|
| Add `Poker_TikZ_card` / `buildPokerTeX` | Dev | ~6.35×8.89 cm; increase safe margins (3–5 mm) for trim |
| Per-card PNG/PDF export | Dev | `pdftoppm` or `pdfcrop` per tikzpicture; or standalone LaTeX per card |
| Bleed | Design | +3 mm bleed if vendor template requires it |
| Proof order | Group | 1 deck ASAP before bulk |
| CMYK proof | Design | Screen colors ≠ linen stock; expect one revision |

### MTG → poker migration note

Dimensions are **almost the same** as Magic (63×88 mm). The real work is **vendor file format** (54 individual uploads) and **typography at poker safe zone**, not a total redesign.

---

## 5. Deck composition & card selection

### Pool

- Start from **[ChessRuleCards](https://github.com/SmoothDragon/ChessRuleCards)** (superset).
- Current **`arcmate.json`** is an early subset (32 cards); several names differ from the Sheet (e.g. “Attack swap” vs `CAPTURE SWAP`).

### Selection criteria (use Sheet rubric + add these)

| Criterion | Target for SDCC |
|-----------|-------------------|
| **Teachable in <2 min** | Prefer cards that need no extra tokens |
| **Composable** | Cards stack via “current rules” model (README master rules) |
| **Bughouse-safe** | Avoid rules that break two-board timing unless tested |
| **No adjudication hell** | Deprioritize “No legality check” = fail in Sheet |
| **1v1 stall** | Deprioritize rules that increase draws in single-board chess |
| **Balance** | Mix `origin` (C/I/F), `genre` (+, T, diff, -) across each 27 |

### Playtest protocol

1. **Single-card smoke test** — deal 1 card, play one game, rate clarity 1–5.
2. **Two-card stack test** — deal 2 (order matters); note conflicts in Sheet “combo notes”.
3. **Bughouse session** — 4 players, 5+5 clocks, record broken rules.
4. **Cut list** — bottom quartile by (fun + clarity) unless strategically kept for expansion identity.

### Deliverable

`docs/CARD_LIST.md` (or Sheet tab) with final **Origins 27** and **Expansion 27**, each row linking to ChessRuleCards commit/line.

---

## 6. Rules, terminology, ambiguity

### Documents to add

| Doc | Purpose |
|-----|---------|
| `GLOSSARY.md` | Single definitions: *orthodox piece*, *acts*, *move vs capture*, *drop*, *genre* badges (C/I/F, +/T/diff) |
| `RULEBOOK.md` → PDF | Comic-Con teach + home play; include Fischer Random dice procedure from README |
| `QUICKREF.md` | One page: deal procedure, stacking, “+” draw rule, bughouse pointer |

### Standardize terminology (decisions)

| Term | Current usage | Proposed standard |
|------|---------------|-------------------|
| Move / capture / act | Mixed on cards | **Move** = relocation; **capture** = removal by rule; **act** = any legal turn action including special |
| “X” / piece classes | `\KI`, `\NoKing`, etc. | Glossary table mapping macros → English |
| Card name | Sheet vs JSON mismatches | One **canonical_id** + display **caption** |
| “Draw extra card” | README: first `+` only | Rulebook must state clearly for demos |

### Ambiguity pass (before print)

- [ ] Every card: **trigger**, **duration** (rest of game vs one turn), **who chooses** targets.
- [ ] Fix duplicate/wrong fields in JSON (e.g. `CROWNED` has two `description` keys — keep one).
- [ ] Rules that need **extra equipment** (10×10 board, cylinder diagram): include **setup diagram** on card or ban for Origins.
- [ ] Document **interaction priority** when two cards conflict (order dealt = order applied unless rulebook says otherwise).

---

## 7. Art & branding

| Asset | Status | Notes |
|-------|--------|-------|
| **Card backs** | Needed | Origins vs Expansion; ChatGPT drafts → repo `art/backs/` |
| **Box / tuck** | Vendor default | Window tuck often included; add logo sticker if needed |
| **Logo / wordmark** | TBD | ArcMate + subtitle for Origins / Expansion |
| **Table banner** | Optional | For SDCC visibility |
| **Rule icons** | In repo | `symbols.tex`, `graphics/` — verify legibility at poker size |

**Process:** Place approved art in repo; reference paths from JSON (`graphic` field pattern already partially supported in `Magic_TikZ_card`).

---

## 8. Comic-Con operations

From [`COMIC_CON_SUBMISSION.md`](COMIC_CON_SUBMISSION.md) — operational checklist:

| Item | Qty / note |
|------|------------|
| Printed decks | ≥2 playable sets + 1 spare |
| Demo boards | Chess + bughouse (or dual demo board) |
| Clocks | 5+5 for advertised length |
| Laminated quick-ref | 4+ copies |
| **Teach script** | 60-second pitch + 3-minute teach |
| **Feedback** | QR → form or Sheet tab “SDCC feedback” |
| **Legal** | Repo licenses: GPL + CC-BY-NC-SA — confirm quotes on cards and NC use at con |

---

## 9. Repository task backlog

### P0 (before print order)

- [ ] Resize / export path for **poker** + vendor upload
- [ ] Finalize **27+27** list; trim `arcmate.json` to match
- [ ] `GLOSSARY.md` + `RULEBOOK.md` v1
- [ ] Spreadsheet ↔ JSON **export** script; agree hybrid workflow with group
- [ ] Cover art in repo; wire backs into print export
- [ ] Proof deck ordered

### P1 (before SDCC)

- [ ] Playtest round 2 on physical cards
- [ ] `QUICKREF` printed
- [ ] Name expansion; update JSON metadata (`deck`: `origins` | `expansion`)
- [ ] README points to PLAN, rulebook, Sheet

### P2 (nice to have)

- [ ] `graphic_cards` populated for heavy visual rules
- [ ] CI: `make` fails if JSON captions ≠ Sheet export
- [ ] Online rules page / repo wiki

---

## 10. Open decisions (resolve in W0–W1)

| # | Decision | Options | Recommendation |
|---|----------|---------|----------------|
| 1 | **Expansion name** | Brainstorm 3–5; vote | Block print/back art until chosen |
| 2 | **54 vs 52+2 layout** | 27+27 strict vs 26+26+jokers | 26+26+2 jokers for printer compatibility |
| 3 | **One deck or two SKUs at con** | Single 54 vs two 27-card products | Single 54 for cost; **sell/play** as two halves |
| 4 | **Quotes on cards** | Keep / shorten / remove for space | Shorten or drop for SDCC; keep in rulebook appendix |
| 5 | **Sheet vs JSON authority** | Hybrid above | Hybrid |
| 6 | **Primary demo mode** | Chess vs bughouse | Teach **chess + 1 card** first; bughouse as “advanced” |
| 7 | **Print quantity** | | ≥3 decks + 1 proof |
| 8 | **ChessRuleCards licensing** | | Confirm SmoothDragon repo license allows derivative deck text |

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

*Last updated: 2026-05-30. Revise timeline when Comic-Con booth dates and printer turnaround are confirmed.*
