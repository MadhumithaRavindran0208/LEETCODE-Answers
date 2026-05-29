class Solution(object):
    def pivotInteger(self, n):
        l=[i for i in range (1,n+1)]
        for i in range (n):
            if sum(l[:i+1])==sum(l[i:]):return l[i]
        else:return -1   