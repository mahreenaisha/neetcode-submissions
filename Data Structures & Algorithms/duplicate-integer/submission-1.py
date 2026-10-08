class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # TC = O(N), SC = O(N)
        hs = set()
        for num in nums:
            if num in hs:
                return True
            hs.add(num)
        return False
            
        