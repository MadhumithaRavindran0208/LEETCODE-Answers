class Solution(object):
    def countCharacters(self, words, chars):
        c=0
        for i in words:
            a=0
            for j in set(i):
                if i.count(j) <= chars.count(j):a+=1
            if a==len(set(i)):c+=len(i)
        return c