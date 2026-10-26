#REVISIT

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we are gonna have a list (called count) of 26 elements, each element representing frequency of an alphabet (a-z) (why dont we use hashmap here?)
        # traverse strs, for each word, reflect the freq of letters in 'count' list, this list will the key and the word will be in the list in the value
        # in python, list cannot be a key. so, convert it into tuple.
        # the words that have the same 'count' dict will be added to the same key
        
        # TC = O(M * N), SC = O(M * N)
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(word)

        return list(res.values())




