# https://leetcode.com/problems/peak-index-in-a-mountain-array/
import math

def mountain_index(arr) -> int:
  # # init soln w/ binary search:
  # i, j = 0, len(arr)-1
  # while(i <= j):
  #   mid = (i+j) // 2
  #   prev = arr[mid-1] if mid != 0 else -1
  #   curr = arr[mid]
  #   nex = arr[mid+1] if mid != len(arr)-1 else math.inf
  #   if(prev < curr and nex < curr):
  #     return mid
  #   elif(prev > curr):
  #     j = mid - 1
  #   else:
  #     i = mid + 1
  # return -1

  # # brute force:
  # for i in range(len(arr)):
  #   if arr[i] > arr[i+1]:
  #     return i

  # cleaner binary search:
  # no need to check both sides, just use logic from brute force
  lo, hi = 0, len(arr) - 1
  while lo < hi:
    mi = (lo + hi) // 2
    if arr[mi] < arr[mi + 1]:
      lo = mi + 1
    else:
      hi = mi
  return lo

def main():
  print(mountain_index([4,10,3,2,1,0]))

if __name__ == '__main__':
  main()