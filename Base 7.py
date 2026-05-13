class Solution(object):
    def convertToBase7(self, num):
        if num==0:return "0"
        n= num<0
        num=abs(num)
        r=""
        while num>0:
            r=str(num%7)+r
            num//=7
        return "-"+r if n else r