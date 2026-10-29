from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        n=len(nums)
        final=[[]]
        for i in range(1,n+1):
            final.extend(list(c) for c in combinations(nums, i))
        return final