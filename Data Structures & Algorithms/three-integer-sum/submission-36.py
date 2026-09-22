class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums)):
            k=len(nums)-1
            j=i+1
            while j<k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0 and [nums[i], nums[j], nums[k]] not in res:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                elif total<0:
                    j+=1
                else:
                    k-=1
        return res 