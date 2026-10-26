class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # optimised approach - one pass
        # TC = O(N), SC = O(N)
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
