import math

n = int(input())
for test in range(n):
  m = int(input())
  x = float(0)
  y = float(0)
  prevangle = 90
  for instruction in range(m):
    deg, dist = map(float, input().split())
    correcteddeg = prevangle + deg
    x = x + dist * math.cos(math.radians(correcteddeg))
    y = y + dist * math.sin(math.radians(correcteddeg))
    prevangle = correcteddeg
  
  print("{:.6f} {:.6f}".format(x,y))
