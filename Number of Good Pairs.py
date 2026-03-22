class Solution(object):
    def numIdenticalPairs(self, nums):
        l=[]
        for i in range (len(nums)):
            for j in range (len(nums)):
                if nums[i]==nums[j] and i<j:
                    l.append((i,j))
        return (len(l))
        