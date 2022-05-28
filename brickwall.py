c = list(map(int, input().split()))
A = list(map(int, input().split()))

def solve(A, c):
  # base case - what is it? - the final brick
  if(len(A) <= 2):
    # if len = 0, just do last check
    if(len(A) == 1):
      if A[0] == 3: return "NO" # if 3 return no (shouldn't even be possible)
      elif A[0] == 2: c[2] -= 1 # then do final check
      elif A[1] == 1: c[1] -= 1 # then do final check
    

  for(c[1] <= 0 and c[2] <= 0 and c[3] <= 0)
  for i in range(1,4):
    if c[i] <= 0: continue  # break if no more bricks of size i left to use
    if i == A[0] : continue
    if i < A[0]: 