class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp=defaultdict(int)
        for n in range(len(numbers)):
            diff=target-numbers[n]
            if diff in mp:
                return [mp[diff], n+1]
            mp[numbers[n]]=n+1
        return []

