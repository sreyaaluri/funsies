# https://leetcode.com/problems/reverse-linked-list/solution/

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

def iterrevlist(head = None) -> ListNode():
  prev = None
  while head:
      lost = head.next 
      head.next = prev
      prev = head
      head = lost
  return prev

def recurrevlist(head = None) -> ListNode():
  if (not head) or (not head.next):
    return head
  # recurring on head's next
  p = recurrevlist(head.next)
  # adjusting head's next pointer
  head.next.next = head
  head.next = None
  return p

def main():
  n13= ListNode(3, None)
  n12 = ListNode(4, n13)
  l1 = ListNode(2, n12)
  l1.print()
  l2 = recurrevlist(l1)
  l2.print()

if __name__ == '__main__':
  main()