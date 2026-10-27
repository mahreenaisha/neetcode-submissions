class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force
        # tc = o(n log n), sc = o(n)
        freqMap = {}
        for n in nums:
            if n in freqMap:
                freqMap[n] += 1
            else:
                freqMap[n] = 1
        sorted_freq_map = dict(sorted(freqMap.items(), key=lambda item: item[1], reverse=True))

        return list(list(sorted_freq_map.keys())[:k])
