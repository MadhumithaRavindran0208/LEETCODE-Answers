class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        sum1=0
        n=len(arr)
        for i in range (1,n+1,2):
            for j in range (n-i+1):
                sum1+=sum(arr[j:i+j])
        return sum1
        