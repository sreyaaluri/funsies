def add(A, size, sum):

  # find inverted numbers
  invA =[]
  for i in range(size):
    num = A[i]
    invnum = ''
    while num > 0:
      d = num % 10
      # if(invert[d] == -1):
      #   invnum = str(num)
      #   break
      invnum += str(d)
      num = num//10
    invA.append(int(invnum))
  # print(invA)


  #check if pairs add to sum
  for i in range(size):
    want1 = sum-A[i]
    want2 = sum-invA[i]
    for j in range(size):
      if(i==j): continue
      if(A[j]==want1 or invA[j]==want1 or A[j]==want2 or invA[j]==want2): return True
  return False

import sys
s = int(input().split()[1])
A = [int(i) for i in input().split()]
print("YES" if add(A, len(A), s) else "NO")

# edge cases : inverse = original, inverse+org = num