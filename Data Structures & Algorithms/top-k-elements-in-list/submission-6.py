class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for n in nums:
            if n not in mp:
                mp[n] = 0
            mp[n] += 1

        #sorting the keys based on the freq count, mp.get is the freq
        sorted_keys = sorted(mp.keys(), key=mp.get, reverse=True)

        return sorted_keys[:k]