class Solution(object):
    def subsetXORSum(self, nums):
        total = 0
        for num in nums:
            total |= num 
        return total * (2**(len(nums)-1))
class Solution(object):
    def subsetXORSum(self, nums):
        total = 0
        for num in nums:
            total |= num  
        return total * (1 << (len(nums) - 1)) 