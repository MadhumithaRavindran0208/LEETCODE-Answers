class Solution(object):
    def isThree(self, n):
        if n<4:return False
        c=0
        for i in range (1,n+1):
            if n%i==0:c+=1
            if c>3:return False
        return c==3
        