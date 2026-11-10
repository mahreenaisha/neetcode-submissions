class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # get compl of a number
        # check if is there in the hashmap
        # if yes, return the current element's index and the compl's index stored in the hashmap
        # if no, store the current element and its index

        numMap = {}
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in numMap:
                return [numMap[compl], i]
            numMap[nums[i]] = i 
