from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
  hashmap = {}
  for i in range(len(nums)):
    better_half = target - nums[i]
    if better_half in hashmap:
      return [i, hashmap[better_half]]
    hashmap[nums[i]] = i

nums = [int(i) for i in input().split(" ")]
target = int(input())
print(two_sum(nums, target))