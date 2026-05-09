class Solution(object):
    def searchInsert(self, nums, target):
        for i in nums :
            if i>=target:
                return (nums.index(i))
        else :
            return (len(nums))
class Solution(object):
    def searchInsert(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left=mid+1
            if nums[mid]>target:
                right=mid-1
        return left
        
