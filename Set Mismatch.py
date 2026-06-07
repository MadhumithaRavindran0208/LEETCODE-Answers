class Solution(object):
    def findErrorNums(self, nums):
        n=len(nums)
        actual_s=sum(nums)
        expected_s=n*(n+1)//2
        unique_s=sum(set(nums))
        duplicate=actual_s-unique_s
        missing=expected_s-unique_s
        return [duplicate,missing]