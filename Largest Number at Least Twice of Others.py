class Solution(object):
    def dominantIndex(self, nums):
        n=max(nums)
        ind=nums.index(n)
        for i in nums:
            if i!=n and n<i*2:ind=-1
        return ind