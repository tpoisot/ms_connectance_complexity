pdf: ms_conn_compl.md
	pandoc ms_conn_compl.md -o ms.pdf --bibliography=/home/tpoisot/texmf/bibtex/bib/local/library.bib --csl=trends.csl --template=template.tex
