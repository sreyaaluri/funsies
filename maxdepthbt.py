# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from collections import deque
import math

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def max_depth(root = TreeNode()) -> int:
  if not root:
    return 0
  stack = deque([(1,root)]) # for DFS
  max_depth = 0             # tracking min depth
  while(stack):
    depth, n = stack.pop()  # get last added node (DFS)
    if(n.left == None and n.right == None):
      max_depth = max(max_depth, depth)
    else:
      if n.left: stack.append((depth+1, n.left))
      if n.right: stack.append((depth+1, n.right))
  return max_depth

def main():
  # make tree
  left = TreeNode(9)
  right = TreeNode(20, TreeNode(15), TreeNode(7))
  tree = TreeNode(3, left, right)
  # run test
  print("Expect: 3, Ans: ", max_depth(tree))

if __name__ == '__main__':
  main()