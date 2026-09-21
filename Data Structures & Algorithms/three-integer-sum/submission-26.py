class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            j=len(nums)-1
            k=i+1
            while(k<j):
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.add(tuple([nums[i], nums[j], nums[k]]))
                    k+=1
                    j-=1
                elif total < 0:
                    k+=1
                else:
                    j-=1
        return [list(i) for i in res]
