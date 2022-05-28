s = input()
sz = len(s)

forwardset = set()
backwardset = set()
forwardnums = [0] * sz
backwardnums = [0] * sz

for i in range(sz):
  forwardset.add(s[i])
  forwardnums[i] = len(forwardset)

for i in range(sz-1, -1, -1):
  backwardset.add(s[i])
  backwardnums[i] = len(backwardset)

numsplits = 0
for i in range(sz-1):
  if(forwardnums[i] == backwardnums[i+1]):
    numsplits += 1

print(numsplits)
