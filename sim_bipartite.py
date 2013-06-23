import numpy as np
import scipy as sp
import scipy.stats as sps
import matplotlib.pyplot as plt

def create_matrix(t, b, l):
  if l < np.max([t, b]):
    l = np.max([t, b])
  if l > t*b:
    l = t*b
  mat = np.concatenate((np.ones(l), np.zeros(t*b-l)))
  FreeNodes = 1
  while FreeNodes > 0:
    np.random.shuffle(mat)
    tmat =  mat.reshape((t, b))
    sa1 = np.sum(tmat, axis=0)
    sa2 = np.sum(tmat, axis=1)
    if np.prod(sa1)*np.prod(sa2) > 0:
      FreeNodes = 0
  return tmat

top = 25
bottom = 25
step = 10
repls = 100

test_links = np.arange(np.max([top, bottom])*2, top*bottom+step, step)
store_out = np.zeros((len(test_links)*repls,10))
index = 0
for tl in test_links:
  print tl
  for repl in xrange(repls):
    result = [tl/float(top*bottom)]
    result.append(repl)
    xx = create_matrix(top, bottom, tl)
    result.append(np.mean(np.sum(xx, axis=0)))
    result.append(np.mean(np.sum(xx, axis=1)))
    result.append(np.var(np.sum(xx, axis=0)))
    result.append(np.var(np.sum(xx, axis=1)))
    result.append(sps.stats.kurtosis(np.sum(xx, axis=0)))
    result.append(sps.stats.kurtosis(np.sum(xx, axis=1)))
    result.append(sps.stats.skew(np.sum(xx, axis=0)))
    result.append(sps.stats.skew(np.sum(xx, axis=1)))
    store_out[index] = result
    index += 1

np.savetxt('bipartites.dat', store_out)
