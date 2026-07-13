class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        for i,j in enumerate(sentence.split()):
            if j.startswith(searchWord):return i+1
        return -1
        