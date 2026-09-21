class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for k,v in enumerate(nums):
            t = target - v
            if t in check:
                return [check[t], k]
            check[v] = k
        return []
