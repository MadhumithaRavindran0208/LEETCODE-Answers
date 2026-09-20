class Solution(object):
    def restoreString(self, s, indices):
        if indices==sorted(indices):return s
        final=[" "]*len(s)
        for i,j in zip(s,indices):
            final[j]=i
        return "".join(final)