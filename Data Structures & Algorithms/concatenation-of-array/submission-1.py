class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=len(nums)
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums