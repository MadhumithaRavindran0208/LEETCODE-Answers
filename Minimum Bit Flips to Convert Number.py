class Solution(object):
    def minBitFlips(self, start, goal):
        c=0
        s=bin(start)[2:]
        g=bin(goal)[2:]
        n=max(len(s),len(g))
        for i,j in zip(s.zfill(n),g.zfill(n)):
            if i!=j:c+=1
        return c
        