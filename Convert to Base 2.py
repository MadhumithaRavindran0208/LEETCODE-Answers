class Solution(object):
    def baseNeg2(self, n):
        if n==0:
            return "0"
        result=[]
        while n!=0:
            r=n%2       
            result.append(str(r))
            n=-(n//2)           
        return "".join(reversed(result))
