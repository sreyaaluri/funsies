# https://leetcode.com/problems/add-two-numbers/

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

def ads_two_numbers(l1 = ListNode(), l2 = ListNode()) -> ListNode():
  # init 1st node of result
  result = ListNode() 
  sum1 = l1.val + l2.val
  result.val = sum1 % 10

  # setup variables for loop
  carry = sum1 // 10
  prev = result
  while(not (l1.next == None and l2.next == None)):
    # updating input number lists
    v1 = 0
    v2 = 0
    if(l1.next != None):
      l1 = l1.next
      v1 = l1.val
    if(l2.next != None):
      l2 = l2.next
      v2 = l2.val
    # initialize current node of sum of input numbers w/ carry
    val = v1 + v2 + carry       # value of current node's sum
    curr = ListNode(val % 10)   # init curr node with sum excluding carry
    # update next of prev node
    prev.next = curr
    # setup for next iter
    carry = val // 10           # update carry
    prev = curr                 # upadate prev node
    
  # add last node if carry is not 0 
  if(carry != 0):
    prev.next = ListNode(carry)
  return result

  """
  Cleaner Soln:
  dummyHead = ListNode(0)
  curr = dummyHead
  carry = 0
  while l1 != None or l2 != None or carry != 0:         set condition for when to run instead of when to end 
    l1Val = l1.val if l1 else 0
    l2Val = l2.val if l2 else 0
    columnSum = l1Val + l2Val + carry
    carry = columnSum // 10
    newNode = ListNode(columnSum % 10)
    curr.next = newNode
    curr = newNode
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
  return dummyHead.next                           NEAT hack! 
  """

def main():
  n13= ListNode(3, None)
  n12 = ListNode(4, n13)
  l1 = ListNode(2, n12)
  n23 = ListNode(4, None)
  n22 = ListNode(6, n23)
  l2 = ListNode(5, n22)
  l1.print()
  l2.print()
  ads_two_numbers(l1,l2).print()

if __name__ == '__main__':
    main()


"""
3 lists
advance all three on each iteration
in an iteration, I want to already have carry value stored
- update l1 to l1.next
- update l2 to l2.next
- add l1+l2+carry 
- store ^ % 10 in next node
- set curr cal to ^ / 10 
- update curr's next to next
- update next as curr

ending the loop:
if l1.next == none and l2.next == none then we can end cuz the carry node will already exist
if they're not none then advance them (so shift updating l1 and l2 to first step in loop)


"""