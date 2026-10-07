class Solution(object):
    def thousandSeparator(self, n):
        s=str(n)
        result=[]
        while len(s)>3:
            result.append(s[-3:])
            s=s[:-3]
        result.append(s)
        return ".".join(reversed(result))
class Solution(object):
    def thousandSeparator(self, n):
        s=str(n)
        result=[]
        n=len(s)
        if n>3:
            for i in range(n,n%3,-3):
                result.append(s[i-3:i])
            if n%3!=0:result.append(s[:n%3])
            return ".".join(reversed(result))
        return s