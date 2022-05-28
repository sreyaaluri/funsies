import copy

def invert(n):
  if(n in [0,1,2,5,8]): return n #same
  if(n==6): return 9
  if(n==9): return 6
  return -1 # invalid invert

def add(A, size, s):
  # append inverted numbers
  others = []
  B = copy.deepcopy(A)
  for num in A:
    invnum = ''
    k = num
    while k > 0:
      d = k % 10
      # if(invert(d) == -1):
      #   invnum = -1 
      #   break
      invnum += str(invert(d))
      k = k // 10
    if invnum != -1 and int(invnum) != num:
        others.append(int(invnum)) #append instead
        B.remove(num)

  #check if pairs add to sum
  l = 0
  r = len(A)
  print(A)
  print(others)
  print(B)

  for i in range(r):
    for k in range(i + 1, r):
      if A[i] +A[k]== s:
        return True
  for i in range(len(others)):
    for k in range(i+1, len(others)):
      if others[i] +others[k]== s:
        return True
  for i in range(len(others)):
    for k in range(len(B)):
      if others[i] +B[k]== s:
        return True
  return False  
  
n, s = input().split()
A = [int(i) for i in input().split()]
if add(A, len(A), int(s)):
    print("YES")
else:
    print("NO")
