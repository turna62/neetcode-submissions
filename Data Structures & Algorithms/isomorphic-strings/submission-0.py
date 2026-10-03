class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        rev = {}
        for c1,c2 in zip(s,t):
            if c1 in mp and mp[c1]!=c2:
                return False
            if c2 in rev and rev[c2]!=c1:
                return False
            mp[c1]=c2
            rev[c2]=c1
        return True