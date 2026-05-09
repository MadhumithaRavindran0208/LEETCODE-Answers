class Solution(object):
    def mySqrt(self, x):
        return(int(x**0.5))
class Solution(object):
    def mySqrt(self, x):
        low = 0
        high = x
        while high >= low:
            mid = (high + low) / 2
            if mid * mid < x:
                low = mid + 1
            elif mid * mid > x:
                high = mid - 1
            else:
                return mid
        return mid if mid * mid < x else mid - 1
