A = [1,2,3,4,5]
l = len(A)
totalload = sum(A)
max_on_one = totalload//2

# DP[i][j] contains load on server 1 using first ith items with maxload j 

DP = [[-float('inf')] * (max_on_one+1) for _ in range(l+1)]

for j in range(max_on_one+1):
  DP[0][j] = 0 # no processes -> no load

for i in range(l+1):
  DP[i][0] = 0 # max load = 0 -> no processes allowed

for i in range(1,l+1):
  for j in range(1,max_on_one+1):
    li = A[i-1] # load of ith process
    withouti = DP[i-1][j]
    withi = DP[i-1][j-li] + li if j-li >= 0 else 0

    DP[i][j] = max(withouti, withi)

diff = abs(totalload - 2 * DP[l][max_on_one])

print(diff)