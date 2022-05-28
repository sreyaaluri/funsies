invert = [0,1,2,-1,-1,5,9,-1,8,6]
s = int(input().split()[1])
A = [int(i) for i in input().split()]

def flip(num):
  x = 0
  while num > 0:
    a = num % 10
    x += 10 ** (len(str(num))-1) * a
    num //= 10
  return x

b=False
for i in range(len(A)):
  value = A[i]
  want1 = s-value
  want2 = s-flip(value)
  A.remove(value)
  if(want1 in A or want2 in A or flip(want1) in A or flip(want2) in A):
    print("YES")
    b=True
    break
  A.insert(i, value)

if not b: print("NO")
