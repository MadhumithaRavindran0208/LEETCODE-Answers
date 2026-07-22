class Solution(object):
    def maxProduct(self, nums):
        if len(nums)==0:return nums[0]
        maxi=max(nums)
        curMax = 1
        curMin = 1
        for i in range(len(nums)):
            temp=curMax*nums[i]
            curMax=max(nums[i],nums[i]*curMax,nums[i]*curMin)
            curMin=min(nums[i],temp,nums[i]*curMin)
            maxi=max(maxi,curMax)
        return maxi