class Solution(object):
    def wordPattern(self, pattern, s):
        p=list(pattern)
        a=s.split(" ")
        r1=zip(a,p)
        if len(a)!=len(p):return (False)
        for i,j in r1:
            if p.index(j)==a.index(i):continue
            else:return (False)
        return (True)