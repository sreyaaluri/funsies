S = "ababbcbc"
l = len(S)

# preprocessing for frequencies
unique_chars = set()
for s in S:
  unique_chars.add(s)

freq = {}
for c in unique_chars:
  freq[c] = [0] * (l+1)

# 1st char
freq[S[0]][1] = 1
print(freq)

# other chars
for i in range(2, l+1):
  for c in unique_chars:
    freq[c][i] = freq[c][i-1]
  freq[S[i-1]][i] = freq[S[i-1]][i] + 1 


