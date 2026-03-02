class Solution(object):
    def findTheDifference(self, s, t):
        for char in t:
            if t.count(char) != s.count(char):
                return char       
        