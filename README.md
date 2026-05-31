# ArcMate
A deck of alternate chess rules. Deal one or two cards. Designed for Fischer Random and bughouse.

**SDCC target:** [ArcMate: Origins](PLAN.md) — **25** rule + **2** reference cards per deck; **54-card print = 2 decks**.

**Docs:** [PLAN.md](PLAN.md) · [RULEBOOK.md](RULEBOOK.md) · [GLOSSARY.md](GLOSSARY.md) · [QUICKREF.md](QUICKREF.md) · [Card list](docs/CARD_LIST.md) · [Playtest ratings](docs/PLAYTEST.md) · Design notes: [arcmate.txt](arcmate.txt)

# How to make
Print out PDF file to make cards.

Sync card text to the group [Google Sheet](https://docs.google.com/spreadsheets/d/1FEswgLlyckdUdkqBpFjGnMcEMd2lOh_IVsh94GkxTQg/edit) (`arcmate_json` tab): see [scripts/README.md](scripts/README.md).

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # once per machine
make setup                                      # uv sync → .venv
export GOOGLE_APPLICATION_CREDENTIALS="$PWD/scripts/secrets/service-account.json"
make sync-sheet   # JSON → Google Sheet
make              # PDF
```

# How to play
Deal one or two cards to modify the rules of chess/bughouse.
The cards are designed to be a mapping from rules to rules, so the card order matters!
Have fun playing!

# Example card rule page
![ArcMate](https://github.com/SmoothDragon/arcmate/blob/main/arcmate.png)

# Master rules
- Rules refer to how a piece currently moves/captures/acts, given the application of previous rules. "Orthodox piece" refers the original piece.
- **No check:** you win if the opponent has no king at the end of your turn (see [RULEBOOK.md](RULEBOOK.md)).
- The "+" indicates extra cards to be drawn. (Optional) Only the first "+" card seen draws additional cards.
- Any piece "moving as a pawn", may be captured en passant.

# Fischer Random 960 (d8, d12, d20)

Full instructions with step-by-step diagrams: [docs/FISCHER_RANDOM_960.md](docs/FISCHER_RANDOM_960.md).  
Example rolls **(6, 9, 16)** → rank 1: **B N R K R Q N B**. Reference card **R2** in the deck.
