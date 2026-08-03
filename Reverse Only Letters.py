class Solution(object):
    def reverseOnlyLetters(self, s):
        s1=[]
        for i in range(len(s)):
            if s[i].isalpha():s1.append(s[i])
        s1=s1[::-1]
        result=""
        j=0
        for i in range(len(s)):
            if s[i].isalpha():
                result+=s1[j]
                j+=1
            else:result+=s[i]
        return result
        