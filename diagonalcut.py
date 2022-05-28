# https://open.kattis.com/contests/ohvbk9/problems/diagonalcut

import math

def computeGCD(x, y):
  while(y):
    x, y = y, x % y
  return x

total = 0

m, n = map(int, input().split()) # m is col, n is row
if(m==n): print(m)
else:
  total = 0
  d = computeGCD(m,n)
  if(d==0 and m%2 != 0 and n%2 != 0): 
    total = 1
  else:
    mp = m//d
    np = n//d
    dp = computeGCD(mp, np)
    if(dp==1 and mp%2 != 0 and np%2 != 0):
      total = d
  print(total)
    


# print(m,n)
# slope = m/n
# left = 0
# right = round(slope,2)  
# for i in range(1, n+1):
#   baseY = math.floor(left)
#   left -= baseY
#   right -= baseY
#   if(abs(left+right-1) < 1e-04): # left+1 == 2-right ohhh they add up to 1! left+right == 1
#     total += 1
#   # print(i,": ", left, " + ", right, " = ", left+right)
#   left = right
#   right = round(right+slope,2)
# print(total)
