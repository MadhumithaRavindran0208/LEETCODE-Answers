class Solution(object):
    def alternateDigitSum(self, n):
        s=0
        for i,j in enumerate(str(n)):
            if i%2==0:s+=int(j)
            else:s-=int(j)
        return s
        