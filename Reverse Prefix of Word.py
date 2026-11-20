class Solution(object):
    def reversePrefix(self, word, ch):
        if ch in word:
            i=word.index(ch)
            word=word[:i+1][::-1]+word[i+1:]
        return word