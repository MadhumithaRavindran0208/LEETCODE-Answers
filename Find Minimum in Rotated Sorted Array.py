class Solution(object):
    def findMin(self, nums):
        return (min(nums))
class Solution(object):
    def findMin(self, nums):
        mini=max(nums)
        for i in nums:
            mini=min(i,mini)
        return mini
               