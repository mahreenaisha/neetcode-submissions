class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # optimised, hashmap
        # tc = o(m*n), sc = o(m*n)
        res = defaultdict(list) # creates a dictionary where every new key automatically gets an empty list as its value

        for word in strs:
            count = [0] * 26 # [0, 0, 0, .... 26 times]
            for c in word:
                count[ord(c) - ord('a')] += 1 # ord() converts a character into its Unicode number
            res[tuple(count)].append(word) # no need to worry about the condition where no word has been added to the value of a key as we are initialising this dict to have empty lists as values
        return list(res.values())
        