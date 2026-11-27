class Solution(object):
    def addSpaces(self, s, spaces):
        final=[]
        prev=0
        for i in spaces:
            final.append(s[prev:i])
            prev=i
        final.append(s[prev:])
        return " ".join(final)