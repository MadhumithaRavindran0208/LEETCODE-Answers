class Solution(object):
    def sortVowels(self, s):
        vowels=[]
        v="AEIOUaeiou"
        for i in s:
            if i in v:vowels.append(i)
        vowels.sort()
        j=0
        final=list(s)
        for i in range(len(s)):
            if final[i] in v:
                final[i]=vowels[j]
                j+=1
        return "".join(final)