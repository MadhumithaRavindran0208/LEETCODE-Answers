class Solution(object):
    def missingNumber(self, nums):
        nums=sorted(nums)
        a=0
        for i in range (len(nums)):
            if nums[i]==i:
                a+=1
            else:
                return (i)
        if a==len(nums):
            return(a)
class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range (len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)
            