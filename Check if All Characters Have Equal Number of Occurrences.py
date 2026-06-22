class Solution(object):
    def areOccurrencesEqual(self, s):
        l=[]
        for i in set(s):
            l.append(s.count(i))
        return (len(set(l))==1)
        