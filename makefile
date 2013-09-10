viewer = zathura
panopts = --bibliography=/home/tpoisot/texmf/bibtex/bib/local/library.bib --csl=oikos.csl --template=template.tex

pdf: ms_conn_compl.md
	pandoc ms_conn_compl.md -o ms.pdf $(panopts) 

view: pdf
	$(viewer) ms.pdf

figure_uni: uni_plots.gpl unipartites.dat niche.dat
	gnuplot uni_plots.gpl
	touch sim_power.png
	touch sim_stats.png

unipartites.dat: sim_unipartite.py
	python2 sim_uniparite.py
	touch unipartites.dat

niche.dat: sim_niche.py
	python2 sim_niche.py
	touch niche.dat

figure_ana: sim_plots.gpl sim_files
	gnuplot sim_plots.gpl
	touch ana_space.png
	touch ana_ratio.png

sim_files: sim_analytical.py
	python2 sim_analytical.py
