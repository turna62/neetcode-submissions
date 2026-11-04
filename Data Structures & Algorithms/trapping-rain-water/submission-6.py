class Solution:
    def trap(self, height: List[int]) -> int:
        pre =[0] * len(height)
        suf =[0] * len(height)
        res=0
        for i in range(1, len(height)):
            pre[i]=max(height[i-1], pre[i-1])
            suf[-i-1]=max(height[-i],suf[-i])
        for i in range(len(height)):
            water=min(pre[i], suf[i])-height[i]
            res+=max(0,water)
        return res