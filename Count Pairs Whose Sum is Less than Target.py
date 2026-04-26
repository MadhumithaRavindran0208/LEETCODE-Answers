class Solution(object):
    def countPairs(self, nums, target):
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<target:c+=1
        return c
        