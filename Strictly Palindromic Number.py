class Solution(object):
    def isStrictlyPalindromic(self, n):
        p=bin(n)
        if p[:]==p[::-1]:
            return(bool(1))
        else:
            return(bool(0))
        