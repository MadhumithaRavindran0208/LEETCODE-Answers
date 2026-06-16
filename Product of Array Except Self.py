class Solution(object):
    def productExceptSelf(self, nums):
        a=1
        for i in range(len(nums)):
            a*=nums[i]
        l=[a]*len(nums)
        for i in range(len(nums)):
            if nums[i]!=0:l[i]=l[i]/nums[i]
            else:
                b=1
                for j in range (len(nums)):
                    if j!=i:b*=nums[j]
                l[i]=b
        return l 