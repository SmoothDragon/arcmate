.PHONY: main clean sync-sheet setup fischer960-diagrams FORCE

TEXTMP=.textmp
GRAPHICS= $(wildcard graphics/*.pdf)
UV ?= uv

main: arcmate.pdf arcmate.png

arcmate.tex: arcmate.tex.py arcmate.json symbols.tex $(GRAPHICS)

%.tex: %.tex.py
	python3 $< > $@

%.pdf: %.tex
	mkdir -p $(TEXTMP)
	latexmk -auxdir=$(TEXTMP) -outdir=$(TEXTMP) -pdflatex='lualatex -halt-on-error -file-line-error -interaction=errorstopmode' -pdf $<
	mv $(TEXTMP)/$@ .

%.png:	%.pdf
	pdftoppm -singlefile -png $< $*

setup:
	./scripts/setup_env.sh

fischer960-diagrams:
	cd scripts && python3 gen_fischer960_diagrams.py

sync-sheet:
	$(UV) run python scripts/sync_json_to_sheet.py

show-sheet-account:
	$(UV) run python scripts/sync_json_to_sheet.py --show-account

clean:
	latexmk -pdf -C
