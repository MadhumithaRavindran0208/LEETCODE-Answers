class Solution(object):
    def firstMissingPositive(self, nums):
        n=len(nums)
        check=[False]*(n+1)
        for i in nums:
            if 0<i<=n:
                check[i]=True
        for i in range(1,n+1):
            if not check[i]:
                return i
        return n+1