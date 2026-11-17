class Solution(object):
    def numberOfSpecialChars(self, word):
        t=set(word.lower())
        c=0
        for i in t:
            if i.upper() in word and i.lower() in word:c+=1
        return c