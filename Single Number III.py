class Solution(object):
    def singleNumber(self, nums):
        l=[]
        for i in nums:
            if nums.count(i)==1:
                l.append(i)
        return (l)
        