class Solution(object):
    def countGoodSubstrings(self, s):
        n=0
        for i in range (0,len(s)-2):
            if len(set(s[i:i+3]))==3:n+=1
        return n