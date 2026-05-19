class Solution(object):
    def isSameAfterReversals(self, num):
        if num==0:return True
        return num%10!=0
        