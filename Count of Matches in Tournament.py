class Solution(object):
    def numberOfMatches(self, n):
        s=0
        while n>=2:
            matches=n//2
            s+=matches
            n-=matches
        return s
        