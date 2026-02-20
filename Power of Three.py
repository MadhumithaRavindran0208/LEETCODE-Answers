class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return(bool(0))
        elif n==1:
            return(bool(1))
        while n%3==0:
            n/=3
        return n==1

        