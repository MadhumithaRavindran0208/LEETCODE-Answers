class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            p1 = self.expand(s, i, i)
            p2 = self.expand(s, i, i + 1)
            res = max(res, p1, p2, key=len)
        return res
    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]