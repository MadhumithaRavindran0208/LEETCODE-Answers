class Solution(object):
    def countPartitions(self, nums):
        c=0
        for i in range(len(nums)-1):
            a=sum(nums[:i+1])-sum(nums[i+1:])
            if a%2==0:c+=1
        return c
