class Solution(object):
    def reverseWords(self, s):
        s1=s.split(" ")
        r=[]
        for i in s1:r.append(i[::-1])
        return " ".join(r)
