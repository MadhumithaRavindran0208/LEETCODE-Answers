class Solution(object):
    def isPerfectSquare(self, num):
        if num**0.5==round(num**0.5):
            return(bool(1))
        else:
            return(bool(0))
        