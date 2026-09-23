class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        win = set()
        l =0
        for r in range(len(s)):
            while s[r] in win:
                win.remove(s[l])
                l+=1
            win.add(s[r])
            length = max(length, len(win))
        return length