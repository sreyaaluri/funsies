import heapq

n, m = map(int, input().split())
data = []
for i in range(m):
  h1, h2 = map(int, input().split())
  data.append((h1, h2))

heapq.heapify(data)

connected = True
connected_houses = {1}
disconnected_houses = set()
while data:
  h1, h2 = heapq.heappop(data)
  if h1 in connected_houses:
    connected_houses.add(h2)
  elif h2 in connected_houses:
    connected_houses.add(h1)
  else:
    connected = False
    disconnected_houses.add(h1)
    disconnected_houses.add(h2)

if(connected):
  print("Connected")
else:
  for house in disconnected_houses:
    print(house)