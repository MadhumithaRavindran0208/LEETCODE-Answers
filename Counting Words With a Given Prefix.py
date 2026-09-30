class Solution(object):
    def prefixCount(self, words, pref):
        c=0
        n=len(pref)
        for i in words:
            if i[:n]==pref:c+=1
        return c