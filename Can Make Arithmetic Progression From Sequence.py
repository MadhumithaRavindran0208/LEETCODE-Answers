class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        d=arr[1]-arr[0]
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]!=d:
                return (bool(0))
        return (bool(1))
        