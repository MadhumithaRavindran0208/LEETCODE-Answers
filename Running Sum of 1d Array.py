class Solution(object):
    def runningSum(self, nums):
        l=[]
        for i in range (1,len(nums)+1):
            l.append(sum(nums[:i]))
        return (l)
        