# https://leetcode.com/problems/path-sum/
from collections import deque
import math

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def has_path_sum(root = TreeNode(), targetSum = 0) -> bool:
  if not root:
    return True if targetSum == 0 else False
  stack = deque([(root.val,root)])    # for DFS
  while(stack):
    path_sum, n = stack.pop()         # get last added node (DFS)
    if (n.left == None and n.right == None) and (path_sum == targetSum):
      return True
    if n.left: stack.append((path_sum + n.left.val, n.left))
    if n.right: stack.append((path_sum + n.right.val, n.right))
  
  # lower space complexity: (unsolved)
  # if you only update pathsum at each level
  # how would you track multiple levels of backtracking?
  # stack = deque([root])
  # path_sum = 0
  # while(stack):
  #   n = stack.pop()
  #   path_sum += n.val
  #   if(n.left == None and n.right == None): # n is leaf node
  #     if path_sum == targetSum: return True
  #     else: path_sum -= n.val
  #   else:                                   # n is not leaf node
  #     if path_sum < targetSum:
  #       if n.left: stack.append(n.left)
  #       if n.right: stack.append(n.right)
  #     else:                                 # path is discarded if non-leaf node gives pathsum >= target
  #       path_sum -= n.val
  return False

def main():
  # make tree
  left = TreeNode(2, TreeNode(3))
  right = TreeNode(4)
  tree = TreeNode(1, left, right)
  # run test
  print("Expect: True, Ans: ", has_path_sum(tree, 6))

if __name__ == '__main__':
  main()