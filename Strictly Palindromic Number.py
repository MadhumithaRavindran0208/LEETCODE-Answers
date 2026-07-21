class Solution(object):
    def isStrictlyPalindromic(self, n):
        def value(num,base):
            final=[]
            while num:
                final.append(str(num%base))
                num=num//base
            return "".join(reversed(final))
        for i in range(2,n-1):
            a=value(n,i)
            if a!=a[::-1]:return False
        return True
            
