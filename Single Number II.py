class Solution(object):
    def singleNumber(self, nums):
        c=0
        num=set(nums)
        for i in num:
            for j in sorted(nums):
                if i==j:
                    c+=1
            if c==1:
                return(i)
            else:
                c=0
            