class Solution(object):
    def thirdMax(self, nums):
        nums=list(set(nums))
        nums.sort(reverse=True)
        if len(nums)>2:
            return(nums[2])
        else:
            return(max(nums))
        