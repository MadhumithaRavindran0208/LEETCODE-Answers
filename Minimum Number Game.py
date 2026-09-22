class Solution(object):
    def numberGame(self, nums):
        nums=sorted(nums)
        final=[]
        for i in range (0,len(nums),2):
            final.append(nums[i+1])
            final.append(nums[i])
        return final