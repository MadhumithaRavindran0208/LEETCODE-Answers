class Solution(object):
    def findPeakElement(self, nums):
        return (nums.index(max(nums)))
class Solution(object):
    def findPeakElement(self, nums):   
        begin = 0
        end = len(nums)-1
        while begin < end:
            if nums[begin] < nums[end]:
                begin += 1
            else:
                end -= 1
        return begin
