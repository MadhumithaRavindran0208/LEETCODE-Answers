class Solution(object):
    def containsDuplicate(self, nums):
        a=set(nums)
        return len(nums)!=len(a)
        