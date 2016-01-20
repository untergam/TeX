PDFLATEX = pdflatex
BIBTEX = bibtex
SECTIONS = $(wildcard Chapters/*.tex)
FIGURES = $(wildcard Figures/*.pdf Figures/*.eps)
NAME = main

all: $(NAME).pdf

$(NAME).pdf: $(NAME).tex $(SECTIONS) $(FIGURES)
	$(PDFLATEX) $(NAME).tex
	$(BIBTEX) $(NAME).aux
	$(PDFLATEX) $(NAME).tex
	$(PDFLATEX) $(NAME).tex

clean:
	rm -f $(NAME).aux
	rm -f $(NAME).bbl
	rm -f $(NAME).blg
	rm -f $(NAME).log
	rm -f $(NAME).out
	rm -f $(NAME).toc
