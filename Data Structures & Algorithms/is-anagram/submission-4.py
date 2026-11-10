class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # tc = o(n), sc = o(n)

        return Counter(s) == Counter(t)