class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR = Counter(ransomNote)
        countM = Counter(magazine)
        for i in countR:
            if countM[i] < countR[i]:
                return False
        return True