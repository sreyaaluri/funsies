import math
from collections import deque

# account for not jump more than twice in a row in the same direction and revisiting
# It also refuses to jump backwards to the location it just came from

# define bfs as bfs is enough for getting shortest path here
def bfs(graph, source, dest):
  graph[source[0]][source[1]] = 0 # mark source dist as 0
  Q = deque([source])
  while Q:
    ui, uj = Q.popleft()
    neighbors = []
    up = ui-1
    down = ui+1
    left = uj-1
    right = uj+1
    
    # this ends up adding the one you just came from too
    if up >= 0 and graph[up][uj] != -1 : neighbors.append([up,uj])
    if down < m and graph[down][uj] != -1: neighbors.append([down, uj])
    if left >= 0 and graph[ui][left] != -1: neighbors.append([ui, left])
    if right < n and graph[ui][right] != -1: neighbors.append([ui, right])

    for vi, vj in neighbors:
      if graph[vi][vj] == math.inf:
        graph[vi][vj] = graph[ui][uj] + 1
        if [vi, vj] == dest:
          return graph[dest[0]][dest[1]] # return distance to dest
        Q.append([vi,vj])
  return -1

# reading input and printing solution
t = int(input())

for x in range(t):
  input()
  m, n = map(int, input().split())
  graph = [[-1]*n for i in range(m)]
  dist = [[math.inf]*n for i in range(m)]
  source = [-1, -1]
  dest = [-1. -1]
  # input graph
  for i in range(m):
    sym = input()
    for j in range(n):
      if sym[j] == 'B': 
        graph[i][j] = -1 # marks blockade
        continue
      if sym[j] == 'D': dest = [i,j]
      elif sym[j] == 'R': source = [i,j]
      graph[i][j] = math.inf # marks acc essible spot (unvisited)
  print(graph)
  print(bfs(graph, source, dest))

# visited = [] # List to keep track of visited nodes.
# queue = []     #Initialize a queue

# def bfs(visited, graph, node):
#   visited.append(node)
#   queue.append(node)

#   while queue:
#     s = queue.pop(0) 
#     print (s, end = " ") 

#     for neighbour in graph[s]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)

# # Driver Code
# bfs(visited, graph, 'A')