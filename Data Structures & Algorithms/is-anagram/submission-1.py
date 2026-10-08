class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    # can't use this in interviews
    # Counter is a data structure like a hashmap that automatically stores the frequency of characters
    # basically a built-in frequency hashmap
    # TC: O(n)
    # SC: O(n)

    return Counter(s) == Counter(t)
      