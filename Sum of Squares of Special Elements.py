class Solution(object):
    def sumOfSquares(self, nums):
        sum1=0
        n=len(nums)
        for i in range (1,n+1):
            if n%i==0:sum1+=nums[i-1]**2
        return sum1