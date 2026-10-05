class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        forw={}
        rev={}
        words=s.split(" ")
        if len(words) != len(pattern):
            return False
        for c1,c2 in zip(pattern, words):
            if c1 in forw and forw[c1]!=c2:
                return False
            if c2 in rev and rev[c2]!=c1:
                return False
            forw[c1]=c2
            rev[c2]=c1
        return True