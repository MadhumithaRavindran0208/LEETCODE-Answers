class Solution(object):
    def alternatingSum(self, nums):
        sum1=sum(nums[::2])
        sum2=sum(nums[1::2])
        return (sum1-sum2)
        