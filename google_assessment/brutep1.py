S = "aabcde"
l = len(S)

# preprocessing for frequencies
unique_chars = set()
for s in S:
  unique_chars.add(s)

freq = {}
for c in unique_chars:
  freq[c] = [0] * (l+1)

for i in range(1, l+1):
  for c in unique_chars:
    freq[c][i] = freq[c][i-1]
  freq[S[i-1]][i] = freq[S[i-1]][i] + 1 

print(freq)

#helper
def calc_len(i, j):
  local_freq = 0
  for c in unique_chars:
    cfreq = freq.get(c)[j] - freq.get(c)[i]
    if cfreq == 0: continue
    if(local_freq==0):
      local_freq = cfreq
    elif(cfreq != local_freq):
        return -1
  return j-i
 
# substring
max_len = -1
for start in range(0, l): 
  for end in range(start+1, l+1):
    local_len = calc_len(start,end)
    if local_len > max_len: max_len = local_len
print(max_len)
