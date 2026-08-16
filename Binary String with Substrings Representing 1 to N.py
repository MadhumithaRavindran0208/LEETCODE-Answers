class Solution(object):
    def queryString(self, s, n):
        if n>len(s)*(len(s)+1)//2:
            return False
        for i in range (1,n+1):
            if (bin(i)[2:]) not in s:return False
        return True
