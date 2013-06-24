pdf: ms_conn_compl.md
	pandoc ms_conn_compl.md -o ms.pdf

unidata: sim_unipartite.py
	python sim_unipartite.py
