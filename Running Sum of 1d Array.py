class Solution(object):
    def runningSum(self, nums):
        l=[]
        for i in range (1,len(nums)+1):
            l.append(sum(nums[:i]))
        return (l)
class Solution(object):
    def runningSum(self, nums):
        l=[nums[0]]
        for i in range (1,len(nums)):
            l.append(l[i-1]+nums[i])
        return (l)
                
