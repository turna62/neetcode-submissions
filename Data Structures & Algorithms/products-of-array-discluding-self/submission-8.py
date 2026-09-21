class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1] * (2 * len(nums))
        pre[-1]=1
        pre[0]=1
        res = []
        for i in range(1, len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
            pre[-i-1] = nums[-i]*pre[-i]

        for j in range(0, len(nums)):
            # reusing pre list to save memory
            res.append(pre[j]*pre[j+len(nums)])
        
        return res





        