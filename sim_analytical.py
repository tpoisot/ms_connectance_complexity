import numpy as np
import scipy as sp
import scipy.misc as sc

def M(n):
  return n*(n-1)/2

def C(n, k):
  return sc.comb(n, k)

def R(n,l):
  total = C(M(n), l)
  reali = total - n * C(M(n-1), l)
  return np.array([l/float(M(n)), total, reali])

n = 10

l_iter = xrange(n+2, M(n)+1)
res_store = np.zeros((len(l_iter), 3))

pos = 0
for l in l_iter:
  res_store[pos] = R(n, l)
  pos += 1

np.savetxt('sim.dat', res_store) 

n_iter = [5, 10, 20, 50]

ratio_store = np.array([0, 0, 0, 0])

for i in xrange(len(n_iter)):
  n = n_iter[i]
  l_iter = xrange(n+1, M(n)+1)
  res_store = np.zeros((len(l_iter), 3))
  pos = 0
  for l in l_iter:
    res_store[pos] = R(n, l)
    pos += 1
  np.savetxt('sim_ratio_'+str(n)+'.dat', res_store)

