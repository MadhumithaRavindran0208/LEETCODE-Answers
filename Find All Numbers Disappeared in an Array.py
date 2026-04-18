class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums1=set(nums)
        l=[]
        for i in range (1,len(nums)+1):
            if i not in nums1:
                l.append(i)
        return l
        