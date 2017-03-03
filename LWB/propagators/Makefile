PDFLATEX = pdflatex
BIBTEX = bibtex
SECTIONS = $(wildcard sections/*.tex)

all: main.pdf

.PHONY: main.pdf
main.pdf: main.tex header.tex $(SECTIONS) uml.png # figs
	$(PDFLATEX) main.tex
	$(BIBTEX) main.aux
	$(PDFLATEX) main.tex
	$(PDFLATEX) main.tex

uml.png: uml.dot
	dot -Tpng $< -o $@

# figs:
# 	$(MAKE) -C figures

clean:
	$(MAKE) clean -C figures
	rm -f *.aux *.bbl *.blg *.log *.out *.toc
