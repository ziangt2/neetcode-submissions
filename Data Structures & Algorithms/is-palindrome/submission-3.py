class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ''
        for c in s:
            if c.isalnum():
                strs += c.lower()
        return strs == strs[::-1]
