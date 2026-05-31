# Fischer Random 960 — dice setup

How to build a Chess960 back rank using **one d8**, **one d12**, and **one d20**. The same rolls are reused where noted (you do not roll again for the second bishop or second knight).

**Reference card:** R2 **FISCHER RANDOM 960** in the deck.  
**Worked example (White rank 1):** rolls **d8 = 6**, **d12 = 9**, **d20 = 16** — diagrams below. Standalone walkthrough: **[FISCHER960_EXAMPLE.md](FISCHER960_EXAMPLE.md)**.

Black places rank 8 by **mirroring** White’s rank 1 (file *a* ↔ *h*, same piece types).

Diagrams use Wikipedia’s [Template:Chess diagram](https://en.wikipedia.org/wiki/Template:Chess_diagram) (Module:Chessboard, Commons Staunton pieces). Sources are in `docs/fischer960/wikitext/*.wiki`.

---

## Square colors on rank 1

Files **a–h** left to right (***a* = file 1**). From White’s side on rank 1:

| File | a | b | c | d | e | f | g | h |
|------|---|---|---|---|---|---|---|---|
| Color | dark | light | dark | light | dark | light | dark | light |

**Queen rule:** The queen starts on a **light** square. If d8 lands on a dark file, swap which color gets labels 1–4 vs 1–3 for bishops (see step 3).

---

## Algorithm (White rank 1)

Each diagram shows **only White’s rank 1** (where pieces are placed). White pieces use standard wiki codes (`ql`, `bl`, `kl`, …); empty squares use `x1`–`x9` for setup labels. The `wikitext/*.wiki` files still use a full 8×8 `{{Chess diagram}}` if you paste into Wikipedia.

### 1. Empty rank

Leave every square empty. Number squares **1–8** on rank 1 (these are the **d8** file choices).

![Step 1](fischer960/step-01-empty.svg)

### 2. Queen (d8)

Roll **d8**. Place the queen on that file (1 = *a* … 8 = *h*). Other squares still show **1–8** (the d8 choices).

*Example: 6 → Queen on **f** (light square); a–e and g–h keep their file numbers.*

![Step 2](fischer960/step-02-queen.svg)

### 3. Label dark squares for the first bishop

Among **empty** squares, number only the **dark** squares **1–4** (left to right). Do **not** label the light squares yet.

*Example: dark empties a, c, e, g → **1–4**.*

![Step 3](fischer960/step-03-dark-labels.svg)

### 4. First bishop (d12, same roll)

Take the **d12** value. Subtract **4** repeatedly until the result is **1–4**. Place a **bishop** on the dark square with that label (or on light 1–4 if the queen used a dark square).

*Example: 9 → 9 − 2×4 = **1** → Bishop on dark **1** (a1).*

![Step 4](fischer960/step-04-bishop1.svg)

### 5. Label light squares for the second bishop

Now number the **empty light** squares **1–3** (left to right).

*Example: light empties b, d, h → **1–3**.*

![Step 5](fischer960/step-05-light-labels.svg)

### 6. Second bishop (d12, same roll again)

Take the **same d12** value. Subtract **3** repeatedly until the result is **1–3**. Place a **bishop** on the light square with that label.

*Example: 9 → 9 − 2×3 = **3** → Bishop on light **3** (h1).*

![Step 6](fischer960/step-06-bishop2.svg)

### 7. Label knight squares

Number the **five** empty squares **1–5** from left to right.

![Step 7](fischer960/step-07-five-labels.svg)

### 8. First knight (d20)

Take the **d20** value. Subtract **5** repeatedly until the result is **1–5**. Place a **knight** on that label.

*Example: 16 → 16 − 3×5 = **1** → Knight on **1** (b1).*

![Step 8](fischer960/step-08-knight1.svg)

### 9. Label again

Number the **four** empty squares **1–4** from left to right.

![Step 9](fischer960/step-09-four-labels.svg)

### 10. Second knight (d20, same roll again)

Take the **same d20** value. Subtract **4** repeatedly until the result is **1–4**. Place a **knight** on that label.

*Example: 16 → 16 − 3×4 = **4** → Knight on **4** (g1).*

![Step 10](fischer960/step-10-knight2.svg)

### 11. King and rooks

Three squares remain. Number them **1–3** from left to right. Place the **king** on **2**, **rooks** on **1** and **3**.

*Example: c1=R, d1=K, e1=R → rank a–h:*

**♗ ♘ ♖ ♔ ♖ ♕ ♘ ♗**

![Step 11](fischer960/step-11-final.svg)

---

## Black

Mirror White’s rank 1 onto rank 8 (standard Chess960 pairing).

---

## Subtract-until rules (quick reference)

| Roll | Use for | Subtract | Until result |
|------|---------|----------|----------------|
| **d8** | Queen file | — | 1–8 (use as-is) |
| **d12** | 1st bishop | 4s | 1–4 (on dark labels, or light if Q on dark) |
| **d12** | 2nd bishop | 3s | 1–3 (on light labels, or dark if Q on dark) |
| **d20** | 1st knight | 5s | 1–5 |
| **d20** | 2nd knight | 4s | 1–4 |
| — | King / rooks | — | K on middle of last three |

---

## Regenerate diagrams

Requires network on first run (Wikimedia Commons piece downloads).

```bash
make fischer960-diagrams
```

This writes:

- `docs/fischer960/wikitext/step-*.wiki` — `{{Chess diagram}}` source you can paste into Wikipedia
- `docs/fischer960/step-*.svg` — rank-1 strip using Commons Staunton art (same colors as the template)
- `docs/fischer960/commons-cache/` — cached `Chessboard480.svg` and `Chess_*t45.svg` files

Piece codes follow [Template:Chess diagram](https://en.wikipedia.org/wiki/Template:Chess_diagram/doc): `kl` = white king, `ql` = white queen, `bl` = white bishop, `nl` = white knight, `rl` = white rook; `x1`–`x9` = numeric labels on squares.

---

*See also [RULEBOOK.md](../RULEBOOK.md) §8.*
