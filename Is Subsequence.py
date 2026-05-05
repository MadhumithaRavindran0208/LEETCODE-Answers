class Solution(object):
    def isSubsequence(self, s, t):
        ind=0
        for i in (s):
            if i in t[ind:]:
                ind=t.index(i,ind)+1
            else:return (False)
        return (True)
        