# ArcMate card list (prototype)

Tracks each card’s **canonical id**, print status in [`arcmate.json`](../arcmate.json), and alignment with [`arcmate.txt`](../arcmate.txt). **Playtest ratings (Adam & Jay-C):** [PLAYTEST.md](PLAYTEST.md).

**SDCC deck ([PLAN.md](../PLAN.md)):** **25** rule + **2** reference = **27** unique faces per Origins deck. **Manufacturer:** one **54-card** print = **two** identical Origins decks (27 + 27). Expansion is post-SDCC.

## Playtest inclusion (Adam & Jay-C)

| Tier | Cards | Action |
|------|-------|--------|
| **A (5/5)** | Ghost (move through friendly), Move twice, Insane cylinder, Micro-manager, Cylinder | Strong **Origins** picks |
| **B (4/5)** | Capture twice, War and Peace, Summoner, Precocious pawns, Possession | **Include**; patch wording per [PLAYTEST.md](PLAYTEST.md) |
| **C (3/5)** | Teleporter | **Cut Origins** / expansion only — degenerates to chess |
| **Pending** | Penalty box | Not rated — smoke test before include |

Full notes and global rules (no check, pawn limits): [PLAYTEST.md](PLAYTEST.md).

**Legend — implementation status**

| Status | Meaning |
|--------|---------|
| **done** | Wording matches `arcmate.txt` intent (or split/renamed as agreed) |
| **in json** | In `arcmate.json`; text still needs glossary pass |
| **pending** | Suggested in `arcmate.txt` but not in JSON yet |
| **fix** | Data bug or duplicate field in JSON |

**Target text** uses [GLOSSARY.md](../GLOSSARY.md) terms. **Printed text** is whatever is in `description` today.

---

## Cards in `arcmate.json` (33)

| canonical_id | caption (JSON) | status | notes / target text from `arcmate.txt` |
|--------------|----------------|--------|----------------------------------------|
| `all_passant` | ALL PASSANT | done | A piece may capture an enemy piece on any square it moved through on the previous turn. |
| `archbishop` | ARCHBISHOP | done | A queen may **only** act like a bishop or a knight. |
| `bishop_knight_swap` | BISHOP KNIGHT SWAP | in json | Weapon swap: bishop↔knight. Align “moves like / captures only like” wording with glossary. |
| `bribe` | BRIBE | done | On your turn you may perform an enemy **pawn** action instead. (+ draw in JSON.) |
| `capture_swap` | CAPTURE SWAP | in json | Generic weapon swap (①②). **Clarify** vs piece-named swaps; `arcmate.txt` asks how this differs from weapon swap — treat as **generic** pair named on card. |
| `capture_twice` | CAPTURE TWICE | done | **4/5** — Two captures, two phases; no-check win rule. |
| `castles_for_everyone` | CASTLES FOR EVERYONE | in json | Non-king X castles with friendly non-king Y on same **rank or file** (confirm rank-only vs file in playtest). |
| `chancellor` | CHANCELLOR | done | A queen may **only** act like a rook or a knight. |
| `checkers` | CHECKERS | done | Pawns move/capture like checkers; forced captures (incl. multi); promotion per JSON. |
| `complicate` | COMPLICATE | in json | Deal two more cards. Meta; not in `arcmate.txt` card list. |
| `crowned_bishop` | CROWNED BISHOP | done | Split from “Crowned”; ① = bishop. A bishop may **also** act like a king. |
| `crowned_rook` | CROWNED ROOK | done | ② = rook. A rook may **also** act like a king. |
| `cylinder` | CYLINDER | done | **5/5** — White first-move advantage noted. |
| `cylinder_restricted` | CYLINDER ⇒ | in json | Restricted cylinder (no act left from POV). Extra card not in `arcmate.txt`; playtest or cut for SDCC. |
| `fast_pawns` | FAST PAWNS | done | Multi-square forward; en passant on path; promotion limit; + draw. |
| `insane_cylinder` | INSANE CYLINDER | done | **5/5** |
| `king_knight_swap` | KING KNIGHT SWAP | in json | Replacement: king↔knight **only** act like the other. |
| `knight_swap` | KNIGHT SWAP | in json | Not in `arcmate.txt`; knight-distance swap — keep or merge with move swap. |
| `lend_me_your_horse` | LEND ME YOUR HORSE | done | Protected by knight → **also** act like knight. |
| `possession` | POSSESSION | done | **4/5** — Protected by knight → act like that knight (not possessor). |
| `micro_manager` | MICRO-MANAGER | done | **5/5** |
| `move_swap` | MOVE SWAP | done | Swap if X could **move** to Y’s square (not capture-to). |
| `move_through_friendly` | MOVE THROUGH FRIENDLY PIECES | done | **5/5** — Ghost rename TBD; rulebook: castling + pawn capture. |
| `move_twice` | MOVE TWICE | done | **5/5** — White not move 1; castling = king move. |
| `queen_king_knight` | QUEEN KING KNIGHT | done | Renamed from Night King Queen. A queen may **only** act like a knight or a king. |
| `queen_rook_swap` | QUEEN ROOK SWAP | in json | Weapon swap queen↔rook. |
| `rearguard` | REARGUARD | done | After a queen move, pawn moves to empty square behind as part of that move. |
| `summoner` | SUMMONER | in json | **4/5** — Bishop summoner may capture; pawn not rank 1 or last. |
| `teleporter` | TELEPORTER | in json | **3/5** — **Cut Origins** unless revised. |
| `ten_by_ten` | TEN BY TEN | in json | Promote on **rank 9** (1–10 numbering). |
| `precocious_pawns` | PRECOCIOUS PAWNS | done | **4/5** |
| `trading_places` | TRADING PLACES | done | Knight and pawn swap; **knight move** (order matters). ② pawn per `arcmate.txt`. |
| `war_and_peace` | WAR AND PEACE | done | **4/5** — Say “done”; castling = king move; rename optional. |

---

## Suggested in `arcmate.txt` — not in JSON yet

| canonical_id | working name | status | target text (summary) |
|--------------|--------------|--------|------------------------|
| `penalty_box` | Penalty box | pending | If opponent’s last action was a capture, you may move the capturing piece to any empty square as your action. |
| `retreater` | Retreater | pending | **Cut** for SDCC (Ultima; `arcmate.txt`). Queen suggestion withdrawn. |

---

## Placeholder cards (① / ②) — resolved assignments

From `arcmate.txt` — use concrete types on printed cards, not ①②:

| card | slot | assigned type(s) |
|------|------|------------------|
| crowned | 1 / 2 | bishop / rook → **split into two cards** (in JSON) |
| move_swap | — | bishop and rook (suggested; JSON still generic `\NoKing`) |
| possession | — | knight |
| summoner | — | bishop ✓ |
| teleporter | — | bishop ✓ |
| trading_places | 1 / 2 | knight / pawn ✓ |
| weapon_swap / capture_swap | 1 / 2 | knight–bishop / rook–queen (suggested; JSON has generic + pair swaps) |

---

## Naming alignment (spreadsheet ↔ JSON)

| spreadsheet / informal | JSON caption |
|--------------------------|--------------|
| All Passant | ALL PASSANT |
| Attack swap | CAPTURE SWAP (or specific *X Y SWAP*) |
| Take twice | CAPTURE TWICE |
| Castles for everyone | CASTLES FOR EVERYONE |
| Rear guard | REARGUARD |
| Ten by ten | TEN BY TEN |
| Night king queen | QUEEN KING KNIGHT |
| Move through friendly pieces | MOVE THROUGH FRIENDLY PIECES → **Ghost?** |

---

## Origins 25 + reference 2 (checklist)

- [ ] Mark exactly **25** `text_cards` as `origins: true` in Sheet/JSON (10 rated A/B so far — 15 more from pool)
- [ ] Lock **R1** (rules) and **R2** (960 dice) text in `reference_cards`
- [ ] Cut **Teleporter**, **retreater**, weak duplicates to free slots
- [ ] Decide **CYLINDER ⇒** vs two cylinders (only one may fit in 25)
- [ ] `make` / print export: **27** unique faces + manifest for **54** upload slots (duplicate each face)
- [ ] Lock **card 1–27 order** (same in both halves of the print)

### Reference cards (`reference_cards` in JSON)

| Slot | caption | Status |
|------|---------|--------|
| **R1** | ARCMATE RULES | draft in JSON |
| **R2** | FISCHER RANDOM 960 | done — algorithm + example 6,9,16; see [FISCHER_RANDOM_960.md](FISCHER_RANDOM_960.md) |

Not shuffled into the rule deck; kept aside or boxed as reference.

---

## JSON maintenance queue

All items applied 2026-05-30 (see git history). New changes go through glossary + this list.

---

*Sync with [PLAN.md](../PLAN.md) §6 and spreadsheet when deck split is decided.*
