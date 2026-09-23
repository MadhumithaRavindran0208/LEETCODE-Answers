class Solution(object):
    def minimumAverage(self, nums):
        avg=[]
        nums=sorted(nums)
        n=len(nums)
        for i in range (n/2):
            avg.append((nums[i]+nums[-(i+1)])/2.0)
        return min(avg)