import numpy as np
import scipy as sp
import scipy.stats as sps
import matplotlib.pyplot as plt
import networkx as nx
import community

fitfunc = lambda p, x: p[0] + p[1] * x
errfunc = lambda p, x, y: y - fitfunc(p, x)

def powerlaw(y):
  s_y = np.sort(y)[::-1]
  X = sp.log10(np.arange(1,len(s_y)+1))
  Y = sp.log10(s_y)
  pinit = [10.0, 0.0]
  out = sp.optimize.leastsq(errfunc, pinit, args=(X, Y), full_output = 1)
  index = out[0][1]
  amp = 10**out[0][0]
  return index

def m(n):
  return n-1

def M(n):
  return n*(n-1)/float(2) 

def Mod(G,usebest=True,l=1):
	D = G.to_undirected()
	dendo = community.generate_dendogram(D, None)
	if usebest:
		level = len(dendo)-1
	else:
		level = l
	partition = community.partition_at_level(dendo,level)
	mod = community.modularity(partition, D)
	for n in G:
		G.node[n]['m'] = partition[n]
	return mod

n = 30
step = 10
repls = 50

test_links = np.arange(m(n)*2, M(n), step)
store_out = np.zeros((len(test_links)*repls,8))
index = 0
for tl in test_links:
  print tl
  for repl in xrange(repls):
    result = [tl/M(n)]
    result.append(repl)
    xx = nx.gnm_random_graph(n, tl)
    d_overall = list(xx.degree().values())
    result.append(np.mean(d_overall))
    result.append(np.var(d_overall))
    result.append(sps.stats.kurtosis(d_overall))
    result.append(sps.stats.skew(d_overall))
    result.append(powerlaw(d_overall))
    result.append(Mod(xx))
    store_out[index] = result
    index += 1

np.savetxt('unipartites.dat', store_out)
