class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # tc = o(n log n), sc = o(n)

        return sorted(s) == sorted(t)