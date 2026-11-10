class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            i need to pick triplets
            the triplets should sum up to 0
            and their indexes must be distinct
            cannot have two same triplets
            return answer in any order

            this is not the brute force solution

            tc = o(n log n) for sort + o(n^2) + o(n^2) because we have two loops. one for the first number, and for the other two numbers, we are doing the "twosum" solution.
            therefore, tc = o(n^2)

            sc = o(1) or o(n) bc sorting takes extra memory in some libraries
        '''

        res = []
        nums.sort() # most imp part - remember 

        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue

            l = i+1
            r = len(nums) - 1

            while(l<r):
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        return res            
            
