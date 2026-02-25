class Solution(object):
    def isPowerOfFour(self, n):
        if n==1:
            return(bool(1))
        elif n<=0:
            return(bool(0))
        while n%4==0:
            n/=4
        return n==1