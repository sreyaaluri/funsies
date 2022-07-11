# https://leetcode.com/problems/range-sum-query-immutable/

nums = [-2, 0, 3, -5, 2, -1]
sums = [nums[0]] * len(nums)
for i in range(1, len(nums)):
  sums[i] = nums[i] + sums[i-1]
print(sums)

def sum_range(left: int, right: int) -> int:
  if(left != 0):
    return(sums[right]-sums[left-1])
  else:
    return sums[right]

'''
Better indexing, fewer ifs: same concept of leaving head blank
sum = new int[nums.length + 1];
for (int i = 0; i < nums.length; i++) {
    sum[i + 1] = sum[i] + nums[i];
}
public int sumRange(int i, int j) {
    return sum[j + 1] - sum[i];
}
'''

print(sum_range(0,5))