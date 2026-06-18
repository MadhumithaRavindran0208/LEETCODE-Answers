class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d={}
        if len(set(nums))==len(nums):return False
        for i,j in enumerate(nums):
            if j in d and abs(i-d[j])<=k:return True
            d[j]=i
        return False
        