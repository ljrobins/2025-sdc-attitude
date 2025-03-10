.PHONY: all open final

all:
	. .venv/bin/activate && python paper_cache.py && python figure_normalize.py
	cd final && rm -f *.aux *.bbl *.blg *.log *.out *.toc *.idx *.lot *.lof *.fls *.fdb* *.bcf *.lol *.run.xml *.snm *.nav && lualatex paper && bibtex paper && lualatex paper && lualatex paper && rm -f *.aux *.bbl *.blg *.log *.spl *.out *.toc *.idx *.lot *.lof *.fls *.fdb* *.bcf *.lol *.run.xml *.snm *.nav *.cb *.cb2 *.upa
	open final/paper.pdf

open:
	open final/paper.pdf

final:
	. .venv/bin/activate && python paper_cache.py && python figure_normalize.py
	cd final && pdflatex paper && bibtex paper && pdflatex paper && pdflatex paper