class Solution(object):
    def tribonacci(self, n):
        l=[0,1,1]
        for i in range (2,n+1):
            a=l[i]+l[i-1]+l[i-2]
            l.append(a)
        return l[n]
        