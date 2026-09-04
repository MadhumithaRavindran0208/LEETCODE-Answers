class Solution(object):
    def isGood(self, nums):
        n=len(set(nums))
        maxi=max(nums)
        if n!=maxi:return False
        if len(nums)!=maxi+1:return False
        return nums.count(n)==2
class Solution(object):
    def isGood(self, nums):
        n=len(set(nums))
        if n!=max(nums):return False
        for i in sorted(nums):
            if i!=n and nums.count(i)==2:return False
        return nums.count(n)==2
        