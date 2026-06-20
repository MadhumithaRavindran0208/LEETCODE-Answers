class Solution(object):
    def sumOfUnique(self, nums):
        n=0
        for i in nums:
            if nums.count(i)==1:n+=i
        return n
        