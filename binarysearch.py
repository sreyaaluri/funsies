def search(nums, target) -> int:
  def recurbsearch(i, j) -> int:
    if(i<j): return -1
    mid = (i+j) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] > target:
      return recurbsearch(i, mid-1)
    else:
      return recurbsearch(mid+1, j)

  def iterbsearch() -> int:
    left, right = 0, len(nums)-1
    while(left <= right):
      mid = (left+right) // 2
      if(nums[mid] == target):
        return mid
      elif nums[mid] > target:
        right = mid-1
      else:
        left = mid+1
    return -1

  # return recurbsearch(0, len(nums)-1)
  return iterbsearch()

def main():
  print(search([-1,0,3,5,9,12], 5))

if __name__ == '__main__':
  main()