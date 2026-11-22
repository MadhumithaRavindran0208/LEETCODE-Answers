class Solution(object):
    def findPermutationDifference(self, s, t):
        c=0
        for i in range(len(s)):
            c+=abs(i-t.index(s[i]))
        return c