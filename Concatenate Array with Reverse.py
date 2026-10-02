class Solution(object):
    def concatWithReverse(self, nums):
        nums+=nums[::-1]
        return nums