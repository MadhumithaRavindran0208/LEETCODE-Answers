class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        nums.reverse()
        return nums[k-1]
        