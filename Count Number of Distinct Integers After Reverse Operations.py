class Solution(object):
    def countDistinctIntegers(self, nums):
        l=nums
        for i in nums[:]:l.append(int(str(i)[::-1]))
        return len(set(l))
        