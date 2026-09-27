class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        k=len(s1)
        d=deque(s2[:k])
        for x in range(k, len(s2)):
            if sorted(d)==s1:
                return True
            d.popleft()
            d.append(s2[x])
        return sorted(d)==s1