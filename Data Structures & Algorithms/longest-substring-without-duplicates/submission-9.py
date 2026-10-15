class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win=set()
        l=0
        length=0
        for i in range(len(s)):
            while s[i] in win:
                win.remove(s[l])
                l+=1
            win.add(s[i])
            length=max(length, len(win))
        return length