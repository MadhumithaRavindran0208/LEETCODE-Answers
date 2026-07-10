class Solution(object):
    def findGCD(self, nums):
        mini=min(nums)
        maxi=max(nums)
        for i in range(mini,0,-1):
            if mini%i==0 and maxi%i==0:return i
        