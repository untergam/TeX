PDFLATEX = pdflatex
BIBTEX = bibtex
SVG2PDF = inkscape -z -T -A

.PHONY: all clean archive

all:  thesis

texfiles = $(wildcard *.tex)
imgfiles = data_layout.pdf selection.pdf writing_dataset.pdf

.PHONY thesis: thesis.pdf

thesis.pdf: $(texfiles) thesis.bbl $(imgfiles)
	$(PDFLATEX) -interaction=nonstopmode -file-line-error thesis.tex
	$(PDFLATEX) -interaction=nonstopmode -file-line-error thesis.tex

thesis.aux: $(texfiles)
	$(PDFLATEX) -interaction=nonstopmode -file-line-error thesis.tex

thesis.bbl: thesis.aux
	$(BIBTEX) thesis

image: $(imgfiles)
    

data_layout.pdf: data_layout.svg
	$(SVG2PDF) $@ $<

selection.pdf: selection2.svg
	$(SVG2PDF) $@ $<

writing_dataset.pdf: writing_dataset.svg
	$(SVG2PDF) $@ $<

clean:
	rm -rf build/
	rm -f *.aux
	rm -f thesis.dvi thesis.idx thesis.ind thesis.ilg thesis.out thesis.toc thesis.pdf thesis.log


