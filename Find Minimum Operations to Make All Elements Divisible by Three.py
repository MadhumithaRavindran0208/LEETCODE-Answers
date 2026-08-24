class Solution(object):
    def minimumOperations(self, nums):
        n=0
        for i in nums:
            if (i-1)%3==0 or (i+1)%3==0:n+=1
        return n
        