class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return(i,j)
                else:
                    continue
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            c=target-nums[i]
            if c in nums[i+1:]:return [i,nums.index(c,i+1)]
