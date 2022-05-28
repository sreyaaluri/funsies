# Python program for implementation of Ford Fulkerson algorithm 
   
from collections import defaultdict 
import math
   
#This class represents a directed graph using adjacency matrix representation 
class Graph: 
   
    def __init__(self,graph): 
        self.graph = graph # residual graph 
        self. ROW = len(graph) 
        #self.COL = len(gr[0]) 
          
    '''Returns true if there is a path from source 's' to sink 't' in 
    residual graph. Also fills parent[] to store the path '''
    def BFS(self,s, t, parent): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.ROW) 
          
        # Create a queue for BFS 
        queue=[] 
          
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
           
         # Standard BFS Loop 
        while queue: 
  
            #Dequeue a vertex from queue and print it 
            u = queue.pop(0) 
          
            # Get all adjacent vertices of the dequeued vertex u 
            # If a adjacent has not been visited, then mark it 
            # visited and enqueue it 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
  
        # If we reached sink in BFS starting from source, then return 
        # true, else false 
        return True if visited[t] else False
              
      
    # Returns tne maximum flow from s to t in the given graph 
    def FordFulkerson(self, source, sink): 
  
        # This array is filled by BFS and to store path 
        parent = [-1]*(self.ROW) 
  
        max_flow = 0 # There is no flow initially 
  
        # Augment the flow while there is path from source to sink 
        while self.BFS(source, sink, parent) : 
  
            # Find minimum residual capacity of the edges along the 
            # path filled by BFS. Or we can say find the maximum flow 
            # through the path found. 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
  
            # Add path flow to overall flow 
            max_flow +=  path_flow 
  
            # update residual capacities of the edges and reverse edges 
            # along the path 
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
  
        return max_flow 

#This^ code is contributed by Neelam Yadav 

#nCr function
def nCr(n,r):
  f = math.factorial
  return f(n) // ( f(r) * f(n-r) )

#function to check if A can win
def canAWin():
  # number of teams
  n = int(input())

  # A will never win if it is not participating in the tournament
  if n == 0: return "no"
  
  # A will always win if it is the only team participating in the tournament
  if n == 1: return "yes"

  # number of wins that each team has
  wins = list(map(int, input().split()))

  # maximum number of wins team A can get if it wins all remaning matches
  a_max = wins[0] + sum(map(int, input().split()))
  
  # if only two teams are playing, A can win if the maximum number of wins it can 
  # get is greater than or equal to the number of wins that the other team already has
  if n == 2: return "yes" if a_max >= wins[1] else "no"
  
  # number of matches that can be played between the teams excluding those involving A
  total_matches = 0

  # number of combinations of teams that can play each other excluding A
  c = nCr(n-1, 2)

  # number of nodes that the matrix should have
  num_vertices = 2 + c + (n-1)

  # constructing a matrix with all initial edge weights as 0 (i.e. no edge exists)
  graph = [[0 for i in range(num_vertices)] for j in range(num_vertices)]

  # variable to keep track of indicies of team pairings in the matrix
  p = 0

  # setup vertex s, the pairings vertices, the vertices of each team, and the edges between these vertices
  for i in range(1,n): 
    input_matches = list(map(int, input().split())) 
    for j in range(i+1,n):
      matches = input_matches[j] # get number of matches played b/w pairing i,j
      total_matches += matches # update total_matches
      p += 1 # update index of pairings
      graph[0][p] = matches # connect vertex s to pairing with edge weight as number of matches to be played by the pairing
      graph[p][c+i] = matches # connect the pairing to one of its teams with edge weight as number of matches to be played by the pairing
      graph[p][c+j] = matches # connect the pairing to another of its teams with edge weight as number of matches to be played by the pairing

  # setup vertex t and the edges between the vertices of each team and t
  for i in range(1,n):
    if(a_max-wins[i] < 0): return "no" # case when the number of wins a team already has is greater than the max wins A can get
    graph[c+i][num_vertices-1] = a_max-wins[i] # connect each team to t with edge weight as max wins the team can have so that team A can win
    
  # construct a graph from the adjacency matrix
  g = Graph(graph)
    
  # source = s, sink = t
  source = 0; sink = num_vertices-1

  # run max-flow from s to t
  return "yes" if g.FordFulkerson(source, sink) == total_matches else "no"

# call the function that checks if A can win and print the result
print(canAWin())