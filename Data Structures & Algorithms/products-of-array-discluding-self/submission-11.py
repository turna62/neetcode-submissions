class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        presuf = [1] * (2 * len(nums))
        res = []
        for i in range(1, len(nums)):
            presuf[i] = presuf[i-1]*nums[i-1]
            presuf[-i-1] = nums[-i]*presuf[-i]

        for j in range(0, len(nums)):
            res.append(presuf[j]*presuf[j+len(nums)])
        
        return res