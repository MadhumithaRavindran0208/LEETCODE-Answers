class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return(bool(0))
        d1={}
        d2={}
        for i, j in zip(s, t):
            if i in d1 and d1[i] != j:
                return False
            if j in d2 and d2[j] != i:
                return False
            d1[i] = j
            d2[j] = i
        return True
class Solution(object):
    def isIsomorphic(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))