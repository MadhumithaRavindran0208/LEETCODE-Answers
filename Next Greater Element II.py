class Solution(object):
    def nextGreaterElements(self, nums):
        result=[]
        n=len(nums)
        for i in range (n):
            found=-1
            for j in range (1,n):
                ind=(i+j)%n
                if nums[ind]>nums[i]:
                    found=nums[ind]
                    break
            result.append(found)
        return result