# https://leetcode.com/problems/same-tree/
from collections import deque
import math

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def same_tree(p = TreeNode(), q = TreeNode()) -> bool:
  if not p and not q: return True
  if bool(p) != bool(q): return False

  stack = deque([(p,q)])
  while stack:
    t1, t2 = stack.pop()
    # check value
    if t1.val != t2.val:
      return False
    # check structure
    t1l, t1r, t2l, t2r = t1.left, t1.right, t2.left, t2.right
    if (bool(t1l) != bool(t2l)) or (bool(t1r) != bool(t2r)): 
      return False
    # append if all okay
    if t1l and t2l: stack.append((t1l, t2l))
    if t1r and t2r: stack.append((t1r,t2r))
  return True
  
  # clean recur:
  # # p and q are both None
  # if not p and not q:
  #   return True
  # # one of p and q is None
  # if not q or not p:
  #   return False
  # if p.val != q.val:
  #   return False
  # return same_tree(p.right, q.right) and same_tree(p.left, q.left)


def main():
  # make tree
  left = TreeNode(9)
  right = TreeNode(20, TreeNode(15), TreeNode(7))
  tree = TreeNode(3, left, right)
  # run test
  print("Expect: True, Ans: ", same_tree(tree, tree))

if __name__ == '__main__':
  main()