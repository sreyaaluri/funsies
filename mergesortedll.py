# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def print(self):
    node = self
    while(node.next != None):
      print(node.val, end=", ")
      node = node.next
    print(node.val, end="\n")
    
def itermergell(l1 = ListNode(), l2 = ListNode()) -> ListNode():
  sorted_list = ListNode(0) # dummy head
  head = sorted_list
  head.next = ListNode(2, ListNode(3, ListNode(4, None)))
  while l1 and l2:
    if l1.val < l2.val:
      head.next = l1
      l1 = l1.next
    else:
      head.next = l2
      l2 = l2.next
    head = head.next
  if l1: head.next = l1
  elif l2: head.next = l2
  return sorted_list.next

def recurmergell(l1 = ListNode(), l2 = ListNode()) -> ListNode():
  # end case
  if l1 is None:
    return l2
  elif l2 is None:
    return l1
  # recursive case
  elif l1.val < l2.val:
    l1.next = recurmergell(l1.next, l2)
    return l1
  else:
    l2.next = recurmergell(l1, l2.next)
    return l2

def main():
  n13= ListNode(4, None)
  n12 = ListNode(3, n13)
  l1 = ListNode(2, n12)
  n23 = ListNode(6, None)
  n22 = ListNode(5, n23)
  l2 = ListNode(4, n22)
  l1.print()
  l2.print()
  print("Merged: ", end="")
  itermergell(l1,l2).print()

if __name__ == '__main__':
    main()