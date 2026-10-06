class Solution:
  def search (self, nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    found = False
    while (start <= end):
      mid = (start + end)//2
      if nums[mid] == target:
        found = True
        return mid
      if nums[mid] > target:
        end = mid - 1
      else:
        start = mid + 1
    if found == False:
      return -1
        