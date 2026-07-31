class Solution(object):
    def lengthOfLIS(self, nums):
        l=[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    l[i]=max(l[i],l[j]+1)
        return max(l)
        