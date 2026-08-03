class Solution(object):
    def reverseStr(self, s, k):
        res=[]
        if len(s)==1:return s
        for i in range (0,len(s),k*2):
            a=s[i:i+k]
            res.append(a[::-1])
            res.append(s[i+k:i+(k*2)])
        return "".join(res)
        