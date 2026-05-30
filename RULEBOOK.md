# ArcMate rulebook (draft v0.2)

Chess with a deck of rule-modifying cards. For definitions see [GLOSSARY.md](GLOSSARY.md). For a one-page teach sheet see [QUICKREF.md](QUICKREF.md). Card inventory: [docs/CARD_LIST.md](docs/CARD_LIST.md). Playtest ratings: [docs/PLAYTEST.md](docs/PLAYTEST.md).

---

## 1. Overview

**ArcMate** changes standard chess (or bughouse) by dealing one or more **rule cards**. Each card patches how pieces **move**, **capture**, and **act**. Cards are meant to **stack**: read them in **deal order**; later cards refer to rules as they already stand.

**Players:** 2 (chess) or 4 (bughouse).  
**Time:** Often 5+5 per player; demos ~10–15 minutes total ([`COMIC_CON_SUBMISSION.md`](COMIC_CON_SUBMISSION.md)).

---

## 2. What you need

- Standard chess set (or two sets for bughouse)
- ArcMate deck ([`arcmate.json`](arcmate.json) → printed PDF)
- Optional: dice for Fischer Random setup (below)
- Optional: clock

---

## 3. Setup

1. **Shuffle** the ArcMate deck.
2. **Deal rule cards** (house defaults for demos):
   - **Learning game:** 1 card.
   - **Standard ArcMate:** 2 cards.
   - **Chaos:** 3+ only if everyone agrees.
3. Turn dealt cards **face up in order**. Read each aloud. Apply each card completely before reading the next.
4. Set up chess pieces:
   - **Orthodox start**, or
   - **Fischer Random** (Chess960-style) using the dice procedure in §8, or
   - As required by a card (e.g. Ten By Ten, Precocious Pawns).
5. If a card says **draw another card**, draw immediately after resolving that card (unless using the optional “first `+` only” rule in §5).

---

## 4. How to play chess under ArcMate

Play proceeds as in chess with these overrides:

### 4.1 Master rules

1. **Current rules:** All rules refer to how a piece **currently** may move, capture, and act, including all dealt cards in order.
2. **Orthodox piece:** The **piece type** the physical piece had at the start of the game (before cards).
3. **Your turn:** You normally make **one action** (one move or one capture), unless a card allows a **compound action** (e.g. Move Twice, Capture Twice, War and Peace).
4. **Winning (no check):** ArcMate does **not** use check or checkmate ([playtest](docs/PLAYTEST.md)):
   - At the **end of your turn**, if you **do not have a king**, you **lose**.
   - Otherwise, at the **end of your turn**, if the opponent **does not have a king**, you **win**.
5. **Draws:** Standard chess draw rules unless a card changes them (king capture ends the game before most draws matter).
6. **En passant:** If a piece **moves like a pawn** (including along a multi-square path), en passant applies as in orthodox chess to that path, unless a card says otherwise (see Fast Pawns on the card list).

### 4.2 Compound actions

Some cards let you make **two actions as one turn** (e.g. two moves, two captures, or one move and one capture). Both must be legal under **current** rules when you start the turn. You may use the same piece twice only if the card does not require **different** pieces and the first action does not make the second illegal.

- **Castling** counts as a **king move** (for Move Twice, War and Peace, and similar).
- **Move Twice:** **White** may **not** use this card on **move 1** (before Black has moved).
- **End of turn:** After a compound action, clearly signal **“turn over”** (tap clock, gesture, or say “done”) before the opponent acts.
- **Capture Twice:** Treat the two captures as **two phases** in order; resolve the first fully before the second.

### 4.3 Pawn rules (global)

Unless a card says otherwise:

1. A pawn may not occupy a rank **behind** its orthodox **starting rank** (no retreat past its start line).
2. Card text that **summons**, **drops**, or **teleports** pawns must respect that limit on the card (e.g. Summoner: not to the first or last rank).
3. On a **10×10** board ([Ten By Ten](docs/CARD_LIST.md)), a pawn **promotes on rank 9** (ranks numbered 1–10 from your side).

### 4.4 Card-specific setup

Cards that change the board or start position (Ten By Ten, Precocious Pawns, Checkers, etc.) apply **after** all dealt cards are known, during setup. See individual entries in [docs/CARD_LIST.md](docs/CARD_LIST.md).

### 4.5 Ghost (move through friendly pieces)

Friendly pieces do not block **movement** (not necessarily captures — confirm on card). Documented interactions to clarify in playtest:

- **Castling** with pieces that move through friends.
- **Pawn captures**, including **en passant**, through or past friendly pieces.

---

## 5. The `+` genre and extra draws

Cards marked **`+`** in the genre corner (and text like “draw another card”) add rules and often instruct you to **draw another rule card**.

**Default (demo-friendly):** When you deal a card with a `+` draw instruction, **draw one extra card** and append it to the end of the deal order.

**Optional house rule (README):** Only the **first** `+` card encountered while dealing causes an extra draw; later `+` cards do not. Announce which rule you use before dealing.

**Complicate** deals **two** more cards (meta card; not a `+` genre badge but similar effect).

---

## 6. Bughouse (four players)

Bughouse is two boards, teams of two, captured pieces passed to a partner as reserves.

- Use the **same dealt ArcMate cards** for both boards unless you agree otherwise.
- **Piece drops** follow bughouse conventions; a card that mentions “drop” or bughouse should say so explicitly (most current cards target standard chess).
- **Clock:** Usually one clock per board; demo slots often 5+5.
- When a card references “your king” or ranks, use the board you are playing on.

Test bughouse interactions in playtest before SDCC; note problems in the [spreadsheet](https://docs.google.com/spreadsheets/d/1FEswgLlyckdUdkqBpFjGnMcEMd2lOh_IVsh94GkxTQg/edit?usp=sharing).

---

## 7. Resolving conflicts

1. **Deal order wins** for stacking (“current rules”).
2. **Replacement** (“only act like”) overrides earlier move/capture options for that piece type unless a later card adds again.
3. **Singular card text** binds all pieces of that type unless the card names specific pieces.
4. If still unclear, pause and agree, or remove the last-dealt card for that session. Log the case for [docs/CARD_LIST.md](docs/CARD_LIST.md).

---

## 8. Fischer Random setup (dice)

Optional start; from README. Place pieces on rank 1 (your back rank) as rolled:

| Step | Roll | Placement |
|------|------|-------------|
| Queen | **d8** | Queen on file 1–8 (roll value) |
| Bishops | **d12** | First bishop: roll % 4 → 1–4 on non-queen-color squares; second bishop: roll % 3 → 1–3 on remaining queen-color squares |
| Knights | **d20** | First knight: roll % 5 on five remaining squares; second knight: roll % 4 on four remaining |
| King and rooks | — | King on the middle square of the last three; rooks on the other two |

Then mirror or place black symmetrically as you would for Chess960.

---

## 9. Card badge guide

| Badge | Meaning |
|-------|---------|
| **C** | Chess / western variant culture |
| **I** | Experimental / idea card |
| **F** | Fairy chess piece types (archbishop, chancellor, etc.) |
| **+** | Additive; often extra draw |
| **T** | Board or terrain change |
| **⇌ / diff** | Swap or differential move vs capture |
| **−** | Restriction |

Symbols on the card face (♞, ♝, diagrams) illustrate piece types; full macro list in [GLOSSARY.md](GLOSSARY.md).

---

## 10. Current deck (prototype)

The printable deck is defined in [`arcmate.json`](arcmate.json). **SDCC target:** **ArcMate: Origins** — **25** rule cards + **2** reference cards per deck; one standard **54-card** print run delivers **two** complete copies — see [PLAN.md](PLAN.md). A future expansion deck is separate.

Wording on printed cards may lag this rulebook; **GLOSSARY.md** and [docs/CARD_LIST.md](docs/CARD_LIST.md) track rewrites from [`arcmate.txt`](arcmate.txt).

---

## 11. Teaching script (60 seconds)

> ArcMate is chess plus one or two rule cards. We deal them in order; later cards stack. There is no check — you win if the opponent has no king at the end of your turn. Usually one move or capture per turn; some cards give two. Say “done” after a double action. Pawns have extra limits — see the rulebook. Plus in the corner means draw another card.

---

## Appendix A — Open rules questions

| Topic | Status |
|-------|--------|
| Check / checkmate | **Resolved** — use king-presence win rule ([PLAYTEST.md](docs/PLAYTEST.md)) |
| Ghost + castling / pawn capture | **Open** — pin down wording after next session |
| Castles for everyone | Rank **or** file per card text |
| War and Peace **rename** | Optional; title likely fine (public domain) but confusing — see playtest notes |
| Cylinder **White advantage** | Balance test or demo disclaimer |
| Teleporter | **Deprioritize** for Origins (degenerates to chess) |
| Capture swap vs weapon swap | Capture swap = generic; named swaps = specific pairs |
| Penalty box | Not playtested this session |

---

*Draft v0.2 — reflects Adam & Jay-C playtest ([docs/PLAYTEST.md](docs/PLAYTEST.md)).*
