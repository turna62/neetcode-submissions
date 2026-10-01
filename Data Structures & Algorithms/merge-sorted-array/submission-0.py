class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=len(nums2)
        for i in range(len(nums2)):
            nums1[-l+i]=nums2[i]
        nums1[:]=sorted(nums1)
        return nums1