# https://leetcode.com/problems/average-of-levels-in-binary-tree/
from typing import List
from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def averageOfLevels(root = TreeNode()) -> List[float]:
  # # iter Bfs:
  # avgs = []           # to store level averages
  # count = 0           # no. nodes in level
  # s = 0               # sum of nodes in level
  # q = deque([root])   # for BFS
  # nex = deque()       # for level tracking
  # while(q):
  #   n = q.popleft()
  #   s += n.val
  #   count += 1
  #   # add node's children to next
  #   if n.left: nex.append(n.left)
  #   if n.right: nex.append(n.right)
  #   # handle level change (if any)
  #   if(not q):
  #     q = nex
  #     nex = deque()
  #     avgs.append(s / count)
  #     count = 0
  #     s = 0
  # return avgs

  # post formatting lessons that remove redundant code
  avgs = []           # to store level averages
  q = deque([root])   # for BFS
  while(q):
    count = 0           # no. nodes in level
    s = 0               # sum of nodes in level
    nex = deque()       # for level tracking
    while(q):           # inner loop to handle level changes
      n = q.popleft()
      s += n.val
      count += 1
      # add node's children to next
      if n.left: nex.append(n.left)
      if n.right: nex.append(n.right)
    q = nex
    avgs.append(s / count)
  return avgs
    

def main():
  # make tree
  left = TreeNode(9, TreeNode(3), TreeNode(4))
  right = TreeNode(20, TreeNode(15), TreeNode(7))
  tree = TreeNode(3, left, right)
  # run test
  print(averageOfLevels(tree))

if __name__ == '__main__':
  main()