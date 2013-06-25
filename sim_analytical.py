import numpy as np
import scipy as sp
import scipy.misc as sc

def M(n):
  return n*(n-1)/2

def log_fac(n):
  S = 0
  for i in range(2,n+1): S += np.log(i)
  return S

def C(n, k):
  return sc.comb(n, k)

def R(n,l):
  total = C(M(n), l)
  reali = total - n * C(M(n-1), l)
  return np.array([l, total, reali])

n = 10

l_iter = xrange(2*n, M(n)+1)
res_store = np.zeros((len(l_iter), 3))

pos = 0
for l in l_iter:
  res_store[pos] = R(n, l)
  pos += 1

np.savetxt('sim.dat', res_store) 
