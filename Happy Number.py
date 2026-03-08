class Solution(object):
    def isHappy(self, n):
        s=set()
        while n!=1 and n not in s:
            s.add(n)
            n=str(n)
            sum1=0
            for i in n:
                sum1+=(int(i)**2)
            n=sum1
        return(n==1)