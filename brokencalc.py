def add(a,b,prev):
  return a+b-prev
def sub(a,b,prev):
  return (a-b)*prev
def mult(a,b):
  return (a*b)**2
def div(a):
  return (a//2 if a%2==0 else (a+1)//2)

prev = 1

n = int(input())
for i in range(n):
  inp = input().split(" ")
  a = int(inp[0])
  op = inp[1]
  b = int(inp[2])
  if op == '*':
    res = mult(a,b)
  if op =='/':
    res = div(a)
  if op == '+':
    res = add(a,b,prev)
  if op == '-':
    res = sub(a,b,prev)
  prev = res
  print(res)
