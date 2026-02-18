class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            i=haystack.find(needle)
            return (i)
        else:
            return (-1)