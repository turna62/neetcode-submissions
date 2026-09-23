class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp={}
        l=0
        res=0
        for r in range(len(s)):
            if s[r] not in mp:
                mp[s[r]]=0
            mp[s[r]]+=1
            replace = (r-l+1) - max(mp.values())
            if replace <= k:
                res = max(res, r - l + 1)
            else:
                mp[s[l]] -= 1
                l+=1
        return res