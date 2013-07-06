pdf: ms_conn_compl.md figure_uni figure_ana
	pandoc ms_conn_compl.md -o ms.pdf --bibliography=/home/tpoisot/texmf/bibtex/bib/local/library.bib --csl=ecology-letters.csl --template=template.tex

figure_uni: uni_plots.gpl unipartites.dat niche.dat
	gnuplot uni_plots.gpl
	touch sim_power.png
	touch sim_stats.png

unipartites.dat: sim_unipartite.py
	python sim_uniparites.py
	touch unipartites.dat

niche.dat: sim_niche.py
	python sim_niche.py
	touch niche.dat

figure_ana: sim_plots.gpl sim_files
	gnuplot sim_plots.gpl
	touch ana_space.png
	touch ana_ratio.png

sim_files: sim_analytical.py
	python sim_analytical.py
