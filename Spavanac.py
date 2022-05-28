inp = input().split(" ")
h = int(inp[0])
m = int(inp[1])

if(m >= 45):
  newm = m-45
  newh = h
else:
  newm = 60-(45-m)
  newh = 23 if h==0 else h-1

print(newh,newm)