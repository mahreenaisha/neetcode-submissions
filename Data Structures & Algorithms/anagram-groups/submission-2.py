class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force
        # sort the words, use dictionary
        # tc = o(m * n log n), sc =  o(m*n)
        anagrams = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]

        return list(anagrams.values())
        