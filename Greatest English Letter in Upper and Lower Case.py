class Solution(object):
    def greatestLetter(self, s):
        a=" "
        for i in set(s):
            if i.lower() in s and i.upper() in s :
                if ord(i.upper())>ord(a):a=i.upper()
        if a==" ":return ""
        else:return a
        