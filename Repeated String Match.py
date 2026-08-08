class Solution(object):
    def repeatedStringMatch(self, a, b):
        times=-(-len(b)//len(a))
        for i in range (times,times+2):
            if b in a*i:return i
        return -1
        