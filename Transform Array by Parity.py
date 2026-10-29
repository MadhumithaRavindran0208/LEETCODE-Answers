class Solution(object):
    def transformArray(self, nums):
        ans=[]
        for i in nums:
            ans.append(i%2)
        return sorted(ans)
        