class Solution(object):
    def isPalindrome(self, s):
        t=0
        s=s.lower()
        for i in s:
            if i.isalpha():
                continue
            else:
                s=s.replace(i,"")
        return s==s[::-1]