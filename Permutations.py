from itertools import permutations
class Solution(object):
    def permute(self, nums):
        n=len(nums)
        l=[]
        for c in permutations(nums,n):
            l.append(list(c))
        return l