LATEX_FLAGS="-synctex=1"

.PHONY all: manual.pdf

.PHONY clean:
	rm -f *.pdf
	rm -f *.log
	rm -f *.pdf_tex
	rm -f *.aux
	rm -f *.pdf~
	rm -f *.tex~
	rm -f *.svg~
	rm -f *.toc

manual.pdf:
	pdflatex $(LATEX_FLAGS) main
	bibtex main
	pdflatex $(LATEX_FLAGS) main
	pdflatex $(LATEX_FLAGS) main
