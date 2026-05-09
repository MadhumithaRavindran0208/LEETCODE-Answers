class Solution(object):
    def searchRange(self, nums, target):
        l=[]
        if len(set(nums))==1 and target in nums: return ([0,len(nums)-1])
        for i in range (len(nums)):
            if nums[i]==target :
                l.append(i)
        if l==[]: return ([-1,-1])
        elif len(l)==1: return (l*2)
        elif len(l)>2: return ([l[0],l[len(l)-1]])
        else: return l
class Solution(object):
    def searchRange(self, nums, target):
        l=[-1,-1]
        if target in nums:
            l[0]=nums.index(target)
            for i in range (len(nums)-1,-1,-1):
                if nums[i]==target:
                    l[1]=i
                    break
        return l
class Solution(object):
    def searchRange(self, nums, target):
        def findLeft():
            left, right = 0, len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid
                    right = mid - 1  # keep searching left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return res
        def findRight():
            left, right = 0, len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid
                    left = mid + 1  # keep searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return res
        return [findLeft(), findRight()]
        
