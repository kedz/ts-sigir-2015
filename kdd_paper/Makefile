PROJECT=root
SRC=$(PROJECT).tex
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