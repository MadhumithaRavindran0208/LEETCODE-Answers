class Solution(object):
    def moveZeroes(self, nums):
        l=[]
        n=len(nums)
        for i in nums:
            if i!=0:
                l.append(i)
        for i in range(len(l),len(nums)):
            l.append(0)
        nums[:]=l[:]
        
        