class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach 3: Sorting
        # Sort both strings and compare them.
        # TC: O(n log n)
        # SC: O(n)

        return sorted(s) == sorted(t)