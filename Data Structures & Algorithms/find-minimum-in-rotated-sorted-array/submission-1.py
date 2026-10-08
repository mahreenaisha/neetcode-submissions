class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force - linear search
        # TC = O(N), SC = O(1)
        minimum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < minimum:
                minimum = nums[i]

        return minimum
        