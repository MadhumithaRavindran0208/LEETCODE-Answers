class Solution(object):
    def truncateSentence(self, s, k):
        l=s.split()
        return(" ".join(l[:k]))