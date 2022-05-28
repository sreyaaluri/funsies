A = [5]

rows = [A[0]]
for i in range(1, len(A)):
  newR = True
  for maxh in rows:
    if A[i] < maxh:
      newR = False
      break
  if(newR):
    rows.append(A[i])

print(len(rows))