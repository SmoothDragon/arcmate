# Playtest notes — Adam & Jay-C

Session notes for deck curation and rule changes. **Inclusion ratings** below drive [CARD_LIST.md](CARD_LIST.md) and [PLAN.md](../PLAN.md).

**Rating scale:** 1–5 fun/clarity for SDCC prototype (5 = strong include).

---

## Inclusion recommendation (tested cards)

| Tier | Rating | Card | SDCC recommendation |
|------|--------|------|---------------------|
| **A — core** | 5/5 | Move through friendly pieces (→ **Ghost**) | **Include** Origins; document castling + pawn interactions |
| **A** | 5/5 | Move twice | **Include**; rule: White cannot use on move 1 |
| **A** | 5/5 | Insane cylinder | **Include** |
| **A** | 5/5 | Micro-manager | **Include** |
| **A** | 5/5 | Cylinder | **Include**; note White first-move advantage |
| **B — strong** | 4/5 | Capture twice (was “take twice”) | **Include**; compound-turn / phase wording |
| **B** | 4/5 | War and Peace | **Include**; rename? (see below); explicit end-of-turn |
| **B** | 4/5 | Summoner (bishop) | **Include**; clarify capture + pawn rank limits |
| **B** | 4/5 | Precocious pawns | **Include** |
| **B** | 4/5 | Possession (knight) | **Include**; add to `arcmate.json`; **no** king possession |
| **C — cut or expansion** | 3/5 | Teleporter (bishop) | **Deprioritize** — often degenerates to normal chess |
| — | — | Penalty box | Not rated this session; add only after smoke test |

### Design principle (from session)

> Rules that **degenerate to ordinary chess** felt less satisfying (Teleporter 3/5).

Add to deck-selection rubric: prefer cards that **change** piece behavior or board topology in obvious ways.

---

## Per-card notes

### Move through friendly pieces — 5/5

- Pin down effects on **castling** and **pawn capture** (en passant, paths).
- Working name **Ghost** still favored ([`arcmate.txt`](../arcmate.txt)).

### Move twice — 5/5

- **White cannot** use this card on **first move** (one compound action before Black moves).
- **Castling** counts as a **king move** (uses the king’s action for that part of the turn).

### Capture twice — 4/5

- Game has **distinct phases** within a compound turn; needs clear “phase 1 / phase 2” or “first capture / second capture.”
- Old question “how does check work?” → superseded by **no-check** win rule (below).

### Insane cylinder — 5/5

- No extra clarifications recorded.

### War and Peace — 4/5

- **Castling** is a king move when paired with move+capture turns.
- In practice, players need a clear **“my turn is over”** signal (pass gesture, tap clock, say “done”) after compound actions.
- **Name / copyright:** *War and Peace* (Tolstoy) is public domain, but the title may confuse players or imply licensed branding. Consider rename: **MOVE AND CAPTURE**, **TWO ACTIONS**, etc. Legal review optional; not a blocker for prototype.

### Summoner (bishop) — 4/5

- A **summoner can capture** (bishop’s summoner action may be a capture, not only a reposition).
- A **pawn cannot be summoned** to the **first or last rank** (see global pawn rules).

### Teleporter (bishop) — 3/5

- Too often plays like normal chess → **cut from Origins** unless a future revision makes the warp mandatory/interesting.

### Precocious pawns — 4/5

- Include; stack with global pawn rules.

### Possession (knight) — 4/5

- Tested as knight possessor; **king possession rejected**.
- Add card to deck; distinguish from **Lend Me Your Horse** in wording (possession vs loaned powers).

### Micro-manager — 5/5

- Include as-is.

### Cylinder — 5/5

- “Hated it in a good way” — high engagement.
- **Balance:** noticeable **White first-move advantage**; test Black compensation or demo disclaimer.

---

## Global rule changes (adopt for v0.2)

### 1. Remove check; king presence wins

Proposed standard (playtest consensus):

1. At the **end of your turn**, if you **do not have a king**, you **lose**.
2. Otherwise, at the **end of your turn**, if the opponent **does not have a king**, you **win**.

No check, checkmate, or “must respond to check” phases. Captures and compound turns are simpler to adjudicate.

**Follow-ups:** Still define when a turn **ends** (especially War and Peace, Capture twice). Illegal self-removal of king should be impossible or instant loss.

### 2. Pawn rules (explicit)

| Rule | Text |
|------|------|
| **Minimum rank** | A pawn may not occupy a rank **behind** its orthodox starting rank (no moving backward past start line). |
| **Magic moves** | Cards that relocate pawns (summon, rearguard, etc.) must state they respect minimum rank / promotion limits on the **card**. |
| **10×10 promotion** | On a 10×10 board, pawns promote on **rank 9** (ranks numbered 1–10 from each player’s perspective). Update **Ten By Ten** card + rulebook. |

### 3. Compound turns

- **Castling** = **king move** (consumes king’s move in Move Twice / War and Peace).
- **End of turn:** After a compound action, player must indicate **turn complete** before opponent acts.
- **Move twice:** White **not** on move 1.

### 4. Degenerate-to-chess filter

When cutting to 27+27, prefer cards rated **4+** that visibly alter play; demote **Teleporter**-style cards unless redesigned.

---

## Untested this session

Cards in [`arcmate.json`](../arcmate.json) not in this report still need ratings (spreadsheet + future sessions): All Passant, Archbishop, Bribe, Capture Swap, Castles for Everyone, Checkers, Complicate, Crowned, Fast Pawns, Knight Swap, Queen King Knight, Rearguard, Ten By Ten, weapon-swap family, etc.

---

## Action items → backlog

| Priority | Task | Owner |
|----------|------|-------|
| P0 | Adopt **no-check** win rule in [RULEBOOK.md](../RULEBOOK.md) + [QUICKREF.md](../QUICKREF.md) | |
| P0 | Add **pawn global rules** to rulebook; patch Summoner, Ten By Ten, Rearguard cards | |
| P0 | Document **Ghost** + castling + pawn capture in rulebook appendix | |
| P1 | ~~Add **Possession** to `arcmate.json`~~ done; refine vs Lend Me Your Horse | |
| P1 | **Cut or move** Teleporter to expansion; fill Origins from Tier A/B | |
| P1 | War and Peace **rename** decision + “turn over” on quick-ref | |
| P2 | Playtest **Cylinder** with Black-first or handicap | |
| P2 | Rate remaining 32-card pool; sync [spreadsheet](https://docs.google.com/spreadsheets/d/1FEswgLlyckdUdkqBpFjGnMcEMd2lOh_IVsh94GkxTQg/edit?usp=sharing) | |

*Recorded: Adam & Jay-C session (date TBD in git).*
