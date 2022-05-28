n,e = map(int, input().split())
pow2 = str(2**e)

count = 0
for i in range(n+1):
  if pow2 in str(i):
    count += 1

print(count)