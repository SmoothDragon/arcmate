# ArcMate rulebook (draft v0.1)

Chess with a deck of rule-modifying cards. For definitions see [GLOSSARY.md](GLOSSARY.md). For a one-page teach sheet see [QUICKREF.md](QUICKREF.md). Card inventory and wording status: [docs/CARD_LIST.md](docs/CARD_LIST.md).

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
3. **Your turn:** You normally make **one action** (one move or one capture), unless a card allows a **compound action** (e.g. move twice, war and peace).
4. **Check and checkmate:** Use current king move/capture powers unless a card removes or alters them. If unclear, agree before the game or consult [docs/CARD_LIST.md](docs/CARD_LIST.md) notes.
5. **Draws:** Standard chess draw rules unless a card changes them.
6. **En passant:** If a piece **moves like a pawn** (including along a multi-square path), en passant applies as in orthodox chess to that path, unless a card says otherwise (see Fast Pawns on the card list).

### 4.2 Compound actions

Some cards let you make **two actions as one turn** (e.g. two moves, two captures, or one move and one capture). Both must be legal under **current** rules when you start the turn. You may use the same piece twice only if the card does not require **different** pieces and the first action does not make the second illegal.

### 4.3 Card-specific setup

Cards that change the board or start position (Ten By Ten, Precocious Pawns, Checkers, etc.) apply **after** all dealt cards are known, during setup. See individual entries in [docs/CARD_LIST.md](docs/CARD_LIST.md).

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

The printable deck is defined in [`arcmate.json`](arcmate.json) (32 rule cards today). Planned retail split: **ArcMate: Origins** and **expansion** (~27 cards each) from a 54-card poker print — see [PLAN.md](PLAN.md).

Wording on printed cards may lag this rulebook; **GLOSSARY.md** and [docs/CARD_LIST.md](docs/CARD_LIST.md) track rewrites from [`arcmate.txt`](arcmate.txt).

---

## 11. Teaching script (60 seconds)

> ArcMate is chess plus one or two rule cards. We deal them in order; later cards change rules on top of earlier ones. On your turn you usually make one move or capture, unless the cards say you can do two things. Words on the cards use our glossary: *move*, *capture*, *act* — not “take” or “attack.” If a card has a plus in the corner, we draw another rule card. Setup is normal chess unless a card says otherwise, like a bigger board or pawns moved forward. Questions on a specific card — read the card aloud and we apply the glossary.

---

## Appendix A — Open rules questions

Track answers here after playtests; several come from [`arcmate.txt`](arcmate.txt):

| Topic | Question | Tentative direction |
|-------|----------|---------------------|
| Castles for everyone | Same **rank** only, or **file** too? | JSON allows rank **or** file |
| Capture swap vs weapon swap | Same card or different? | Capture swap = generic; piece-pair swaps = specific weapon swaps |
| Protection basis | Move-based vs capture-based? | Glossary uses capture-based until playtest says otherwise |
| Penalty box / Possession | Not in JSON yet | See card list |

---

*Draft v0.1 — align with `arcmate.txt` and spreadsheet before Comic-Con print.*
