class Solution(object):
    def findDuplicate(self, nums):
        s=set()
        for i in nums:
            if i not in s:s.add(i)
            else:return i