class Solution(object):
    def divide(self, dividend, divisor):
        if dividend== divisor:
            return (int(1))
        elif pow(2,31)*-1<dividend and divisor<pow(2,31)-1:
            a=1
        elif not(pow(2,31)*-1<dividend) and divisor<0:
            dividend=(pow(2,31)*-1)+1
        elif not(pow(2,31)*-1<dividend) :
            dividend=(pow(2,31)*-1)
        if dividend>0 and divisor>0:
            return(dividend/divisor)
        elif dividend<0 and divisor <0:
            return(abs(dividend)/abs(divisor))
        elif dividend<0 or divisor <0:
            return((abs(dividend)/abs(divisor))*-1)
        elif dividend==0 or divisor==0:
            return (int(0))
            