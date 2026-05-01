class Solution(object):
    def firstUniqChar(self, s):
        c={}
        for i in set(s):
            c[i]=s.count(i)
        for i,j in (enumerate(s)):
            if c[j]==1:return i
        else:return (-1)
        