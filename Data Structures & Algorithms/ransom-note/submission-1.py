class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp={}
        mp1={}
        for m in range(len(magazine)):
            if magazine[m] not in mp:
                mp[magazine[m]]=0
            mp[magazine[m]]+=1
        for m in range(len(ransomNote)):
            if ransomNote[m] not in mp1:
                mp1[ransomNote[m]]=0
            mp1[ransomNote[m]]+=1
        for k,v in mp1.items():
            if k in mp:
                if v > mp[k]:
                    return False
            else:
                return False
        return True
