from math import sqrt

def main():
  N = 10
  res = []

  if N % 2 != 0:
      return []

  x = int((-1 + sqrt(1 + 4 * N)) // 2)

  for i in range(1, x):
      res.append(i*2)

  res.append(N - ((x - 1) * x))

  return res


print(main())