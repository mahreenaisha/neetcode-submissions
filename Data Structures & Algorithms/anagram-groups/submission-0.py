class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force
        # sort and add to dictionary
        # TC = O(M * N LOG N), SC = O(M * N)
        # M - no. of words, N - maximum length of words
        # O(N LOG N) - time comp of sorted() method
        anagrams = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        
        return list(anagrams.values())