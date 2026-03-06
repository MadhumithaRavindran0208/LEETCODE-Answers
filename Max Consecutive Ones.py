class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n=0
        nl=[]
        for i in range (len(nums)):
            if nums[i]==1:
                n+=1
            if nums[i]==0:
                nl.append(n)
                n=0
            if i==(len(nums)-1):
                nl.append(n)
        return (max(nl))
        