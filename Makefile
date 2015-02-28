PROJECT=acl2015
ALGOSRC=algorithm/ap.tex algorithm/filtering.tex algorithm/introduction.tex algorithm/novelty.tex algorithm/salience.tex
SRC=$(PROJECT).tex $(ALGOSRC) algorithms.tex introduction.tex methods.tex motivation.tex notation.tex paper.tex relatedwork.tex experiments.tex
TARGET=$(PROJECT).pdf
$(TARGET):$(SRC)
	pdflatex --shell-escape $(SRC)
	bibtex acl2015.aux
	pdflatex --shell-escape $(SRC)
	pdflatex --shell-escape $(SRC)

clean:
	rm -f \
		$(PROJECT).aux \
		$(PROJECT).bbl \
		$(PROJECT).blg \
		$(PROJECT).log \
		$(PROJECT).pdf \
        docfreq.pdf \
        docfreq.pdf_tex
