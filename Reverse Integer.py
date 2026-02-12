class Solution(object):
    def reverse(self, x):
        num=str(x)
        if x<0:
            num=str(abs(x))
            a=int(num[::-1])*-1
        elif x>0:
            a=(int(num[::-1]))
        else:
            a=x
        if a>(-2**31) and a<(2**31)-1:
            return(a)
        else:
            return 0