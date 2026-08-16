class Solution(object):
    def maxRotateFunction(self, nums):
        maxi=float("-inf")
        for k in range (len(nums)):
            nums[:]=nums[1:]+[nums[0]]
            a=0
            for i,j in enumerate(nums):
                a+=i*j
            maxi=max(a,maxi)
        return maxi  
class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        S = sum(nums)
        current = sum(i * v for i, v in enumerate(nums))
        maxi = current
        for k in range(1, n):
            last = nums[n - k]
            current = current + S - n * last
            maxi = max(maxi, current)
        return maxi 