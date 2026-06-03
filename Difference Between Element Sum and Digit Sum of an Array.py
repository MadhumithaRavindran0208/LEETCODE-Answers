class Solution(object):
    def differenceOfSum(self, nums):
        a=sum(nums)
        c=0
        for i in nums:
            for j in str(i):c+=int(j)
        return abs(a-c)
class Solution(object):
    def differenceOfSum(self, nums):
        a=sum(nums)
        c=0
        for i in nums:
            while i>9:
                c+=i%10
                i//=10
            else:c+=i
        return abs(a-c)
   