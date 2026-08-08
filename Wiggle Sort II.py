class Solution(object):
    def wiggleSort(self, nums):
        result=[]
        nums.sort()
        nums1=sorted(nums,reverse=True)
        small=nums[:(len(nums)+1)//2][::-1] 
        large=nums1[:len(nums)//2]            
        for i in range(len(large)):
            result.append(small[i])
            result.append(large[i])
        if len(small)>len(large):            
            result.append(small[-1])
        nums[:]=result
        return nums
class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        mid=(len(nums)+1)//2
        left,right=nums[:mid][::-1],nums[mid:][::-1]
        nums[::2],nums[1::2]=left,right
        return nums