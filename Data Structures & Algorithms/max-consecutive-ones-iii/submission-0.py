class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length=0
        l=0
        for r in range(len(nums)):
            k-=(1 if nums[r]==0 else 0)
            while k<0:
                k+=(1 if nums[l]==0 else 0)
                l+=1
            length=max(length, r-l+1)
        return length