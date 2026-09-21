class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        uniq = set()
        length = {0}

        if not nums:
            return 0

        for n in nums:
            if n not in uniq:
                uniq.add(n)

        uniq1 = sorted(uniq)

        if len(uniq1) == 1:
            return 1

        for i in range(1, len(uniq1)):
            if uniq1[i] == uniq1[i-1] + 1:
                count += 1
                length.add(count)
            else:
                count =1
                length.add(1)

        return max(length)