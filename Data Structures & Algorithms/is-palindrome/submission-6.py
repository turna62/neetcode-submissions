class Solution:
    def isPalindrome(self, s: str) -> bool:

        st = ""

        for x in s:
            if x.isalnum():
                st += x.lower()

        return st == st[::-1]

        