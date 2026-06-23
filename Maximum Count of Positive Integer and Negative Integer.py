class Solution(object):
    def maximumCount(self, nums):
        mini,maxi=0,0
        for i in nums:
            if i<0:maxi+=1
            if i>0:mini+=1
        return max(mini,maxi)
        