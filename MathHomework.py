# https://open.kattis.com/contests/wmr34u/problems/mathhomework

b, d, c, l = map(int, input().split())
flag = False
# xb + yd + zc = l
for x in range(l+1):
  for y in range(l+1):
    if((l-x*b-y*d) / c == (l-x*b-y*d)//c and (l-x*b-y*d) >= 0): 
      flag = True
      print(x, y, (l-x*b-y*d)//c)

if not flag:
  print("impossible")