class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0]*len(arr)
        rMax=-1
        for i in range(len(arr)-1, -1, -1):
            res[i]=rMax
            rMax=max(rMax, arr[i])
        return res
