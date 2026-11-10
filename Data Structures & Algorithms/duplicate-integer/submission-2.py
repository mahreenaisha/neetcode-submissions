class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # tc = o(n)
        # sc = o(n)
        numSet = set()
        for i in range(len(nums)):
            if (nums[i] in numSet):
                return True
            numSet.add(nums[i])

        return False