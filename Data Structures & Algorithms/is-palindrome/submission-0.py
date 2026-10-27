class Solution:
    def isPalindrome(self, s: str) -> bool:
        # brute force 
        # tc = o(n), sc = o(n)

        """
        s = s.strip().lower()
        check_string = ""
        for c in s:
            if c.isalnum():
                check_string += c
        if check_string == "".join(reversed(check_string)):
            return True
        else:
            return False
        """

        clean_str = "".join(char.lower() for char in s if char.isalnum())
        return clean_str == clean_str[::-1]

'''
NOTES:
brute force 
tc = o(n), sc = o(n)
'''
        