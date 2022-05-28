# https://open.kattis.com/contests/ohvbk9/problems/freefood

days = [False]*365
n = int(input())

for i in range(n):
  s, t = map(int, input().split())
  for i in range(s-1,t):
    days[i] = True

sum = 0
for x in days:
  sum += x

print(sum)
