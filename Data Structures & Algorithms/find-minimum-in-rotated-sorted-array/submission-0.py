class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force
        # learnt that sorted() does not modify the original list
        # TC = O( N LOG N), SC = O(N)
        nums = sorted(nums)
        return nums[0]
        