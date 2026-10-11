class Solution(object):
    def numberOfSpecialChars(self, word):
        upper=[]
        for i in word:
            if i.isupper():upper.append(i)
        c=[]
        for i in set(upper):
            ind=word.index(i)
            if i.lower() in word[:ind] and i.lower() not in word[ind+1:]:c.append(i)
        return len(c)