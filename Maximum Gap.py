class Solution(object):
    def maximumGap(self, nums):
        max1=0
        nums.sort()
        for i in range (len(nums)-1):
            max1=max(max1,nums[i+1]-nums[i])
        return max1