import numpy as np
import scipy as sp
import scipy.stats as sps
import matplotlib.pyplot as plt
import networkx as nx

def m(n):
  return n-1

def M(n):
  return n*(n-1)/float(2) 

n = 25
step = 10
repls = 50

test_links = np.arange(m(n)*2, M(n), step)
store_out = np.zeros((len(test_links)*repls,6))
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
    store_out[index] = result
    index += 1

np.savetxt('unipartites.dat', store_out)
