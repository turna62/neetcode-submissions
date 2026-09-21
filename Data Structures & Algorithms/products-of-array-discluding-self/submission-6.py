class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1] * len(nums)
        suf = [1]* len(nums)
        i = 1
        suf[-1]=1
        pre[0]=1
        for i in range(1, len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
            suf[-i-1] = nums[-i]*suf[-i]

        for j in range(0, len(nums)):
            pre[j]=pre[j]*suf[j]
        
        return pre





        