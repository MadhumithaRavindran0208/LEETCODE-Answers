class Solution(object):
    def isPowerOfTwo(self, n):
        if n==1:
            return (bool(1))
        elif n<=0:
            return (bool(0))
        while n%2==0:
            n/=2
        return n==1