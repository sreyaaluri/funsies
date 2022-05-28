# https://open.kattis.com/contests/wmr34u/problems/inquiryi
# Needs to be linear time. 

n = int(input())
sums = []
squaresums = []
for i in range(n):
  num = int(input())
  if i == 0:
    sums.append(num)
    squaresums.append(num**2)
  else:
    sums.append(num+sums[i-1])
    squaresums.append(num**2 + squaresums[i-1])

max = -1
for i in range(n):
  part1 = squaresums[i]
  part2 = sums[len(sums)-1] - sums[i]
  val = part1 * part2
  if val > max: 
    max = val

print(max)