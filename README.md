# ArcMate
A deck of alternate chess rules. Deal one of two cards. Designed to work with Fischer Random Bughouse.

**Docs:** [PLAN.md](PLAN.md) · [RULEBOOK.md](RULEBOOK.md) · [GLOSSARY.md](GLOSSARY.md) · [QUICKREF.md](QUICKREF.md) · [Card list](docs/CARD_LIST.md) · Design notes: [arcmate.txt](arcmate.txt)

# How to make
Print out PDF file to make cards.

# How to play
Deal one or two cards to modify the rules of chess/bughouse.
The cards are designed to be a mapping from rules to rules, so the card order matters!
Have fun playing!

# Example card rule page
![ArcMate](https://github.com/SmoothDragon/arcmate/blob/main/arcmate.png)

# Master rules
- Rules refer to how a piece currently moves/takes/acts, given the application of previous rules. "Orthodox piece" refers the original piece.
- The "+" indicates extra cards to be drawn. (Optional) Only the first "+" card seen draws additional cards.
- Any piece "moving as a pawn", may be taken en passant.

# Fisher 960 from dice roll of d8, d12, d20
- d8 places Q on position 1-8
- d12 roll of X places first B on one of four non-queen color squares by X%4 (values in 1-4)  
- - X places second B on one of three queen color squares by X%3 (values in 1-3)  
- d20 roll of X places first N on one of five remaining squares by X%5 (values in 1-5)  
- - X places second N on one of four remaining squares by X%4 (values in 1-4)  
- K is placed in center of three remaining squars and a R in the other two on each side
