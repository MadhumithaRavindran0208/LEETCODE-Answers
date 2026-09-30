class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        l=[0]*len(A)
        for i in range (len(A)):
            c=set(A[:i+1])&set(B[:i+1])
            l[i]=len(c)
        return l
        