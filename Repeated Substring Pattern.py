class Solution(object):
    def repeatedSubstringPattern(self, s):
        l=[]
        if len(s)==1:return False
        for i in range (1,(len(s)/2)+1):
            a=s[0:i]
            if str(a*(len(s)/i))==s:return True 
        else:return False      
        