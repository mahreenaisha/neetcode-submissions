class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # optimised solution - frequency hashmap 
        # tc = o(n), sc = o(n)

        # remember to think about base cases first so that the most obvious test cases do not pass in the initial part of the problem
        # for example, if the length of s and t are different, they obviously are not anagrams

        # base case
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        # build both the maps in one for loop as they both are of same length
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for c in countS: # iterates through the keys
            if countS[c] != countT.get(c, 0):
                return False

        return True