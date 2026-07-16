class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        s11=s1.split()
        s22=s2.split()
        l=[]
        for i in s11:
            if s11.count(i)==1 and i not in s22:l.append(i)
        for i in s22:
            if s22.count(i)==1 and i not in s11:l.append(i)
        return l