# https://open.kattis.com/contests/ohvbk9/problems/splat

import math

c = int(input())

for i in range(c):
  colors = []
  n = int(input())
  for j in range(n):
    inpt = input().split()
    x = float(inpt[0])
    y = float(inpt[1])
    r = math.sqrt(float(inpt[2])/math.pi)
    colors.append([inpt[3],x,y,r])
  
  m = int(input())
  for k in range(m):
    u, v = map(float, input().split())
    color = "white"
    for col,x,y,r in colors:
      if(abs(math.sqrt((u-x)**2 + (v-y)**2)) <= r):
        color = col
    print(color)
