PROJECT=paper
ALGOSRC=algorithm/ap.tex algorithm/filtering.tex algorithm/introduction.tex algorithm/novelty.tex algorithm/salience.tex
SRC=$(PROJECT).tex $(ALGOSRC) algorithms.tex introduction.tex methods.tex motivation.tex notation.tex paper.tex problemdefinition.tex relatedwork.tex 
TARGET=$(PROJECT).pdf
$(TARGET):$(SRC)
	pdflatex $(SRC)
	bibtex $(PROJECT)
	pdflatex $(SRC)
	pdflatex $(SRC)

clean:
	rm -f \
		$(PROJECT).aux \
		$(PROJECT).bbl \
		$(PROJECT).blg \
		$(PROJECT).log \
		$(PROJECT).pdf
