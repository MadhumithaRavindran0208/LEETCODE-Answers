class Solution(object):
    def makeFancyString(self, s):
        final=[""]*len(s)
        for i in s:
            n=len(final)
            if n>=2 and final[n-1]==final[n-2]==i:continue
            else:final.append(i)
        return "".join(final)
