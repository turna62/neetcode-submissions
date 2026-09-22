class Solution:
    def trap(self, height: List[int]) -> int:
        pre =[0] * len(height)
        suf =[0] * len(height)
        k=0
        p=0
        res=0
        for i,v in enumerate(height):
            k=max(k,height[i])
            pre[i]=k
        for i in range(len(height)-1,-1,-1):
            p=max(p,height[i])
            suf[i]=p
        for i,v in enumerate(height):
            res+= min(pre[i],suf[i])-v
        return res
