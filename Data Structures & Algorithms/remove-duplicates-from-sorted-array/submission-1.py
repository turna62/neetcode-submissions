class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = set(nums)
        nums[:]=sorted(list(check))
        return len(nums)