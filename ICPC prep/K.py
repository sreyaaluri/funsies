from sys import stdin

n,k = [int(x) for x in input().split()]
S = [0]*n
D = [[0] * 2 for i in range(n)]
print(D)

if k <= n: 
  print(n)
  exit(0)

S[0] = n
for line in stdin:
  v1, v2 = [int(x)-1 for x in line.split()]
  D[v1][0] += 1
  D[v2][0] += 1

  if(D[v1][0] >= D[v2][0]):
    S[D[v1][0]] += 1
    S[D[v2][0]] += 1
    D[v2][1] = D[v1][0]
  else:
    S[D[v2][0]] += 1
    S[D[v1][0]] += 1
    D[v1][1] = D[v2][0]

  print("S", S)
  print("D", D)