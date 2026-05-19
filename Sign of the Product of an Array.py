class Solution(object):
    def arraySign(self, nums):
        s=1
        for i in nums:s*=i
        if s<0:return -1
        elif s>0:return 1
        else:return 0
class Solution(object):
    def arraySign(self, nums):
        if 0 in nums:return 0
        c=0
        for i in nums :
            if i<0:c+=1
        if c%2==0:return 1
        else:return -1 