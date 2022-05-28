n = input()
cards = [int(x) for x in input().split()]
cards.sort()

s = 0
for i in range(len(cards)):
  if i > 0 and cards[i] == cards[i-1]+1: 
    continue
  s += cards[i]
  # print(s, cards)

print(s)
