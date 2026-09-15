class Solution(object):
    def separateDigits(self, nums):
        num=""
        for i in nums:
            num+=str(i)
        result=[]
        for i in num:
            result.append(int(i))
        return result