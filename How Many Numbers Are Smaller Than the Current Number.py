class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        l=[]
        s=sorted(nums)
        for i in range (len(nums)):
            l.append(s.index(nums[i]))
        return (l)
        