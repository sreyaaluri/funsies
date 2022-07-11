# https://leetcode.com/problems/palindrome-linked-list/

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

def isPalindrome(self, head: Optional[ListNode]) -> bool:
  # get middle node
  mid = self.middleNode(head)
  rev = self.in_place_reverse(mid)
  # check palindrome
  while head and rev:
    if(head.val != rev.val):
      return False
    head = head.next
    rev = rev.next 
  return True

            
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
  slow = head      # n
  fast = head.next # 2n
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  return slow.next # either abandon perfect mid in odd or return 2nd mid in even

def in_place_reverse(head = None) -> ListNode():
  prev = None
  while head:
      lost = head.next 
      head.next = prev
      prev = head
      head = lost
  return prev

def main():
  n13= ListNode(3, None)
  n12 = ListNode(4, n13)
  l1 = ListNode(2, n12)
  l1.print()
  l2 = in_place_reverse(l1)
  l2.print()

if __name__ == '__main__':
    main()
