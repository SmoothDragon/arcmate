# ArcMate glossary

Authoritative definitions for rules text, the rulebook, and card wording. Based on [`arcmate.txt`](arcmate.txt); card text in [`arcmate.json`](arcmate.json) should converge on these terms.

**Style rules (always)**

- Do **not** use *take* or *attack* — use **capture**, **move**, and **act** instead.
- Prefer **singular** on cards (“A knight may…”) over plural (“Knights may…”).
- Distinguish **addition** vs **replacement** (see [Acting like another piece](#acting-like-another-piece)).

---

## Board

| Term | Definition |
|------|------------|
| **Square** | One of the 64 squares on a standard board (more if a card enlarges the board). |
| **Adjacent** | One of the up to eight squares that share a **vertex** with a given square (king moves one square to an adjacent square). |
| **Edge-adjacent** | One of the up to four squares that share an **edge** with a given square (rook moves along edge-adjacent squares on a rank or file). |
| **Rank** | A horizontal row of squares. Ranks are numbered so that **rank 1** is nearest the player whose turn it is. |
| **File** | A vertical column of squares. |
| **Behind** | Relative to the direction a piece last moved or faces; used on cards such as Rearguard (define in setup when ambiguous). |

---

## Pieces

| Term | Definition |
|------|------------|
| **Piece** | Any chess piece, **including** pawn and king. (Unlike some chess books, “piece” here is not “everything except pawns.”) |
| **Non-king piece** | Any piece that is not a king. |
| **Non-pawn piece** | Any piece that is not a pawn. |
| **Non-king non-pawn piece** | Any piece that is neither king nor pawn. |
| **Piece type** | One of the six starting types: king, queen, rook, bishop, knight, pawn. |
| **Orthodox piece** | The piece type a physical piece **started the game as**, before any rule cards. Used when a card refers to “original” behavior. |
| **Possessor** | A piece type named on a card as granting protection or borrowed powers (e.g. knight possessor on Lend Me Your Horse). |

On cards and in [`symbols.tex`](symbols.tex), macros such as `\NoKing`, `\Bishop`, `\Knight` denote piece types or restrictions.

---

## Actions, moves, and captures

| Term | Definition |
|------|------------|
| **Action** | Something you may do on your turn. Initially this is a **move** or a **capture**; cards may add other actions. Every action is designated as an **X move** or **X capture** for some piece X (the piece that “owns” the action for timing and card text). |
| **Move** | An action that changes the board and is **not** a capture. After an **X move**, some square that contained X is empty (X relocated). Castling is a **king move**. Promotion is a **pawn move**. |
| **Capture** | An action that removes at least one **enemy** piece from the board. Every capture is an **X capture** for some piece X. After an **X capture**, some square that contained X is empty (X moved onto the captured square, or the capture is defined otherwise by the card). |
| **Act** | To perform an action (move, capture, or other card-granted action). “May act as a knight” means the piece may use knight moves and/or knight captures as allowed by the card. |

**Do not say:** “take a move,” “attack,” “take twice.”  
**Do say:** “make a move,” “capture,” “make two captures.”

---

## Acting like another piece

| Wording | Meaning |
|---------|---------|
| **X may also act like Y** | **Addition:** X keeps its current move and capture options and gains those of Y (as specified). |
| **X may only act like Y** | **Replacement:** X loses previous move/capture options for purposes of that card and uses only Y’s (as specified). |
| **X moves like X but captures only like Y** | **Weapon swap** pattern: movement unchanged; capture uses Y’s capture geometry only. |

Cards should state whether en passant, castling, or promotion count as “acting like” a pawn when relevant.

---

## Protection

| Term | Definition |
|------|------------|
| **Protected** | Piece **Y** is **protected by** friendly piece **X** if X could **capture** Y were Y an enemy piece on its square (using X’s current capture options). |

*Open design note:* protection could instead be defined using moves rather than captures; pick one in the rulebook and use it consistently ([`arcmate.txt`](arcmate.txt) leans toward capture-based).

---

## Cards and deck

| Term | Definition |
|------|------------|
| **Rule card** | A card that modifies chess rules for the current game. |
| **Deal order** | Order in which cards are turned face-up and read; **later cards apply on top of earlier ones** unless the rulebook says otherwise. |
| **Genre badge** (corner) | Rough category: `+` additive/extra draw, `T` terrain/board, `\diff` differential swap, `-` restriction, `$\\varnothing$` meta (e.g. Complicate). |
| **Origin badge** (corner) | Provenance hint: `C` chess variant culture, `I` idea/experimental, `F` fairy chess. Not a separate rules layer. |
| **`+` on card** | After this card is dealt, **draw one additional rule card** (see [RULEBOOK.md](RULEBOOK.md) for the “first `+` only” house option). |

---

## Names to avoid or replace

| Old / informal | Preferred |
|----------------|-----------|
| Take, take twice | Capture, capture twice |
| Attack swap | Capture swap / weapon swap (see [docs/CARD_LIST.md](docs/CARD_LIST.md)) |
| Night king queen | **QUEEN KING KNIGHT** (renamed) |
| Move through friendly pieces | Working name; **Ghost** suggested in [`arcmate.txt`](arcmate.txt) |
| ① / ② placeholders | Concrete types on card (e.g. Knight and Pawn for Trading Places) |

---

## Canonical card IDs

`snake_case` ids in [docs/CARD_LIST.md](docs/CARD_LIST.md) match spreadsheet rows and future sync scripts. Display names match `caption` in `arcmate.json` where possible.
