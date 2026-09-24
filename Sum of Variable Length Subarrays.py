class Solution(object):
    def subarraySum(self, nums):
        final=0
        for i in range(len(nums)):
            start=max(0,i-nums[i])
            final+=sum(nums[start:i+1])
        return final
        