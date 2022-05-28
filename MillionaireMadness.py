# time limit exceed, submitted nikita's for now

from heapq import heappush, heappop
# import time

m, n = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(m)]

laddersizes =  [[(float('inf'), False)]*n for _ in range(m)]

def neighbors(r,c):
  neighbors = []
  if(r-1 >= 0 and not laddersizes[r-1][c][1]): neighbors.append([r-1,c])
  if(r+1 < m and not laddersizes[r+1][c][1]): neighbors.append([r+1,c])
  if(c-1 >= 0 and not laddersizes[r][c-1][1]): neighbors.append([r,c-1])
  if(c+1 < n and not laddersizes[r][c+1][1]): neighbors.append([r,c+1])
  return neighbors

# def modified_dijkstra():

#initializing priority queue and start dist
PQ = []
heappush(PQ, (0,[0,0]))
laddersizes[0][0] = (0,False)
while PQ:
  # print(PQ)
  # time.sleep(1)
  currlad, (r,c) = heappop(PQ)                              # pop node from PQ
  if(not laddersizes[r][c][1]):                             # if node not visited
    for i,j in neighbors(r,c):
      stepsize = mat[i][j]-mat[r][c]
      diff = stepsize-currlad 
      newlad = currlad if diff <= 0 else currlad+diff
      existinglad = laddersizes[i][j][0]
      if(newlad < existinglad):
        laddersizes[i][j] = (newlad, False)                   # update laddersize if better
        heappush(PQ, (newlad, [i,j]))                         # add unvisited neighbors to PQ
      laddersizes[r][c] = (currlad, True)                   # mark node as visited

print(laddersizes[m-1][n-1][0])

# i -> row, j -> column


# nikita's soln:
from collections import defaultdict
import heapq as heap

class Node:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.cost = val

    def __gt__(self, other):
        return self.cost > other.cost

def dijkstra(r, c, mat):
    dist = [[float('inf')] * c for _ in range(r)]
    dist[0][0] = 0
    pq = []
    start = Node(0, 0, 0)
    heap.heappush(pq, start)
    while pq:
        node = heap.heappop(pq)
        x, y, cost = node.x, node.y, node.cost
        if cost > dist[x][y]:
            continue

        if x - 1 >= 0:
            new_cost = mat[x - 1][y] - mat[x][y]
            if new_cost <= 0: new_cost = 0
            new_cost = max(new_cost, cost)
            if new_cost < dist[x - 1][y]:
                dist[x - 1][y] = new_cost
                heap.heappush(pq, Node(x - 1, y, new_cost))

        if x + 1 < r:
            new_cost = mat[x + 1][y] - mat[x][y]
            if new_cost <= 0: new_cost = 0
            new_cost = max(new_cost, cost)
            if new_cost < dist[x + 1][y]:
                dist[x + 1][y] = new_cost
                heap.heappush(pq, Node(x + 1, y, new_cost))

        if y - 1 >= 0:
            new_cost = mat[x][y - 1] - mat[x][y]
            if new_cost <= 0: new_cost = 0
            new_cost = max(new_cost, cost)
            if new_cost < dist[x][y - 1]:
                dist[x][y - 1] = new_cost
                heap.heappush(pq, Node(x, y - 1, new_cost))

        if y + 1 < c:
            new_cost = mat[x][y + 1] - mat[x][y]
            if new_cost <= 0: new_cost = 0
            new_cost = max(new_cost, cost)
            if new_cost < dist[x][y + 1]:
                dist[x][y + 1] = new_cost
                heap.heappush(pq, Node(x, y + 1, new_cost))

    return dist[r - 1][c - 1]

r, c = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(r)]

print(dijkstra(r, c, mat))