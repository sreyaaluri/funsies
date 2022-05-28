import math

# # DP nCr - doesn't work
# nmax = 100//3 + 2#math.ceil(2*n/3)
# rmax = 25 + 1 #n/2
# comb = [[1]*rmax]*nmax
# #base
# for n in range(nmax): 
#   comb[n][0]=1
#   for r in range(1,rmax):
#     if r==n: comb[n][r]=1
#     else: comb[n][r]=comb[n-1][r]+comb[n-1][r-1]

# problem
P = int(input())

# Returns factorial of n
def fact(n):
  res = 1
  for i in range(2, n+1):
    res = res * i
  return res

# Returns nCr
def nCr(n, r):
    return (fact(n) // (fact(r) * fact(n - r)))

for p in range(P):
  K,S = map(int, input().split())
  n = S//2
  totalways = 0
  for i in range(math.ceil(n/3), math.floor(n/2)+1):
    totalways += nCr(n-i,i)**2
  print(K, totalways)
