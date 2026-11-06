class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        take one element
        calculate complementary
        check if it is there in the set
        if yes, then return the index of the current element and the index of the complementary in the set
        if no, add the current element in the set
        this will be tc = o(n), sc = o(n) 
        [one pass, hashmap]

        brute force would be tc = o(n^2), sc = o(1)
        two loops 

        '''

        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        return

        