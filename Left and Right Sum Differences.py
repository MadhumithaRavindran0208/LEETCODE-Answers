class Solution(object):
    def leftRightDifference(self, nums):
        n=len(nums)      
        left=[0]*n
        right=[0]*n
        result=[0]*n
        if n==1:return [0]
        for i in range (n-1):
            left[i+1]=sum(nums[:i+1])
            right[i]=sum(nums[i+1:])
        for i in range(n):
            result[i]=abs(left[i]-right[i])
        return result
class Solution(object):
    def leftRightDifference(self, nums):
        left = [0]
        right = []
        n = len(nums)
        result = []
        if n == 1:
            return left
        for i in range(n - 1):
            left.append(sum(nums[:i+1]))   
            right.append(sum(nums[i+1:]))  
        right.append(0) 
        for i, j in zip(left, right):
            result.append(abs(i - j))
        return result