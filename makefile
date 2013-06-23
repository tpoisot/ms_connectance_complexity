pdf: ms_conn_compl.md bipdata
	pandoc ms_conn_compl.md -o ms_conn_compl.pdf

bipdata: sim_bipartite.py bipartites.dat
	python sim_bipartite.py
