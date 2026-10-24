from itertools import permutations
class Solution(object):
    def permuteUnique(self, nums):
        l=[]
        for c in set(permutations(nums)):
            l.append(list(c))
        return l