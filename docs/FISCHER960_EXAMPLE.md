# Fischer Random 960 — worked example

**Dice:** one **d8**, one **d12**, one **d20** (reuse the same d12 and d20 for both bishops and both knights).

**This example:** **d8 = 6**, **d12 = 9**, **d20 = 16**

Build **White’s rank 1** (files **1–8**, *a* = 1). Each diagram shows only rank 1; captions match the generated SVGs. Full rules: [FISCHER_RANDOM_960.md](FISCHER_RANDOM_960.md).

**Result (a–h):** ♗ ♘ ♖ ♔ ♖ ♕ ♘ ♗

---

## Step 1 — Empty rank

Squares numbered **1–8** for the queen roll (**d8**).

![Step 1](fischer960/step-01-empty.svg)

## Step 2 — Queen (d8 = 6)

**d8 = 6** → Queen on file **6** (*f*, light square). Other squares still show **1–8**.

![Step 2](fischer960/step-02-queen.svg)

## Step 3 — Label dark squares

On empty squares, label **dark** squares **1–4** (left to right). Light squares stay unlabeled.

![Step 3](fischer960/step-03-dark-labels.svg)

## Step 4 — First bishop (d12 = 9)

**d12 = 9** → 9 − 2×4 = **1** → Bishop on dark **1** (*a1*).

![Step 4](fischer960/step-04-bishop1.svg)

## Step 5 — Label light squares

Label empty **light** squares **1–3** (left to right).

![Step 5](fischer960/step-05-light-labels.svg)

## Step 6 — Second bishop (d12 = 9 again)

Same **d12 = 9** → 9 − 2×3 = **3** → Bishop on light **3** (*h1*).

![Step 6](fischer960/step-06-bishop2.svg)

## Step 7 — Label knight squares

Number the **five** empty squares **1–5** (left to right).

![Step 7](fischer960/step-07-five-labels.svg)

## Step 8 — First knight (d20 = 16)

**d20 = 16** → 16 − 3×5 = **1** → Knight on **1** (*b1*).

![Step 8](fischer960/step-08-knight1.svg)

## Step 9 — Label again

Number the **four** empty squares **1–4** (left to right).

![Step 9](fischer960/step-09-four-labels.svg)

## Step 10 — Second knight (d20 = 16 again)

Same **d20 = 16** → 16 − 3×4 = **4** → Knight on **4** (*g1*).

![Step 10](fischer960/step-10-knight2.svg)

## Step 11 — King and rooks

Three squares left → **1–3**. **Rook** on **1**, **king** on **2**, **rook** on **3** (*c1*, *d1*, *e1*).

![Step 11](fischer960/step-11-final.svg)

---

## Black

Mirror White’s rank 1 onto rank 8 (file *a* ↔ *h*, same piece types).

---

*Diagram sources: `fischer960/wikitext/step-*.wiki`. Regenerate: `make fischer960-diagrams` from the repo root.*
