class Solution:
    def trap(self, height: List[int]) -> int:
        pre =[]
        suf =[0]*len(height)
        p=0
        s=0
        res=0
        for i in range(len(height)):
            p=max(p,height[i])
            pre.append(p)
        for i in range(len(height)-1,-1,-1):
            s=max(s,height[i])
            suf[i]=s
        for i in range(len(height)):
            res+=min(pre[i],suf[i])-height[i]
        return res