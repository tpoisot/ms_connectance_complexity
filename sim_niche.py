##
import numpy as np
import scipy as sp
import scipy.stats as sps
import networkx as nx

fitfunc = lambda p, x: p[0] + p[1] * x
errfunc = lambda p, x, y: y - fitfunc(p, x)

def powerlaw(y):
  s_y = np.sort(y)[::-1]
  X = sp.log10(np.arange(1,len(s_y)+1))
  Y = sp.log10(s_y)
  pinit = [10.0, 0.0]
  out = sp.optimize.leastsq(errfunc, pinit, args=(X, Y), full_output=1)
  index = out[0][1]
  amp = 10**out[0][0]
  return index

def m(n): return n-1

def M(n): return n*(n-1)/float(2) 

def niche_foodweb(S, C):
  G = nx.DiGraph()
  G.add_nodes_from([n for n in xrange(S)])
  while np.prod(G.degree().values()) == 0:
    ## Step 1 - create random species
    for n in G:
      G.node[n]['n'] = np.round(np.random.uniform(),2)
      G.node[n]['r'] = np.random.beta(1, 1/float(2*C)-1) * G.node[n]['n']
      G.node[n]['c'] = np.random.uniform(G.node[n]['r']/float(2),G.node[n]['n'])
    ## Step 2 - smallest species are basal
    Smallest = np.min([G.node[n]['n'] for n in G])
    for n in G:
      if G.node[n]['n'] == Smallest:
	G.node[n]['r'] = 0
    ## Step 3 - create the links
    for n1 in G:
      for n2 in G:
	if G.node[n2]['n'] <= G.node[n1]['c']+G.node[n1]['r']:
	  if G.node[n2]['n'] >= G.node[n1]['c']-G.node[n1]['r']:
	    G.add_edge(n1, n2)
    ## Step 4 - remove self edges
    for n in G:
      if G.has_edge(n, n):
	G.remove_edge(n, n)
  return G

S = 30
repls = 50
c_iter = np.linspace(start = 0.05, stop=0.3, num=15)
result_store = np.zeros((repls*len(c_iter),7))
pos = 0
for c in c_iter:
  for r in xrange(repls):
    print "Co "+str(c)+" - repl "+str(r)
    tweb = niche_foodweb(S, c).to_undirected()
    result = [c, tweb.number_of_edges()/float(M(S))]
    d_ov = tweb.degree().values()
    result.append(np.mean(d_ov))
    result.append(np.var(d_ov))
    result.append(sps.stats.kurtosis(d_ov))
    result.append(sps.stats.skew(d_ov))
    result.append(powerlaw(d_ov))
    result_store[pos] = result
    pos += 1

np.savetxt('niche.dat', result_store)
