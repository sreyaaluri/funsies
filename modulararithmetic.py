def extended_gcd(a, b):
    if a == 0:
        return(b, 0, 1)

    unPrev = 1
    vnPrev = 0
    unCur = 0
    vnCur = 1

    while b != 0:
        bn = a // b
        newB = a % b
        a = b
        b = newB

        # Update coefficients
        unNew = unPrev - bn * unCur
        vnNew = vnPrev - bn * vnCur

        # Shift coefficients
        unPrev = unCur
        vnPrev = vnCur
        unCur = unNew
        vnCur = vnNew

    return(a, unPrev, vnPrev)

while True:
  n, t = map(int, input().split())
  if(n==0 and t==0): break

  for i in range(t):
    x, op, y = input().split()
    x = int(x)
    y = int(y)
    if op == '+':
      print((x+y)%n)
    if op == '-':
      print((x-y)%n)
    if op == '*':
      print((x*y)%n)
    if op == '/':
      d, s, t = extended_gcd(y,n)
      if(d != 1): print(-1)
      else:
        print((x*s)%n)
    


# Notes:
# y^-1 is actually y^-1 mod n. y^-1 mod n is the value for which y y^-1 mod n = 1.
# Eg: if n = 13, y = 2, y^-1 mod n for y is 7 because 2*7 = 14 and 14 mod 13 = 1.
# extended_gcd(a,b) returns d, s, t. 
# d is the gcd 
# s and t are ints such that sa + tb = d
# for y to have a y^-1 mod n, y and n have to be relatively prime (cuz otherwise y^-1 cannot give a remainder of 1)
#   i.e. their gcd must be 1
# from extended gcd, if sy+tn = d then sy mod n = 1 mod n (cuz tn is multiple n and d = 1)
#   i.e. s is y^-1 mod n