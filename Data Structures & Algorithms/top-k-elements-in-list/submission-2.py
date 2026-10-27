class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # optimised - bucket sort
        # tc = o(n), sc = o(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
'''
NOTES:
create frequency hash map of nums array. create list (called freq) of size same as nums array - it is a list of lists. it’s index will be the count and values will be a list of elements that have the same frequency as the index. 

traverse through the hashmap.items() make the bucket sort.

traverse the freq list in reverse and stop when the res size is same as k.

tc = o(n) - traversing nums, then count, freq

sc = o(n) - hashmap, freq, res
'''
        