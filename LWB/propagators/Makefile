PDFLATEX = pdflatex
BIBTEX = bibtex
SECTIONS = $(wildcard sections/*.tex)

all: main.pdf

main.pdf: main.tex header.tex $(SECTIONS) # figs
	$(PDFLATEX) main.tex
	$(BIBTEX) main.aux
	$(PDFLATEX) main.tex
	$(PDFLATEX) main.tex

# figs:
# 	$(MAKE) -C figures

clean:
	$(MAKE) clean -C figures
	rm -f *.aux *.bbl *.blg *.log *.out *.toc
