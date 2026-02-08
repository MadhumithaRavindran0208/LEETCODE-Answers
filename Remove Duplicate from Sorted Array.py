class Solution(object):
    def removeDuplicates(self, nums):
        a=sorted(set(nums))
        nums[:]=list(a)
        return (len(nums))