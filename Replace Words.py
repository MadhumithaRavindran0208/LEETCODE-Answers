class Solution(object):
    def replaceWords(self, dictionary, sentence):
        words=sentence.split(" ")
        dictionary.sort(key=len)
        for ind,w in enumerate(words):
            for j in dictionary:
                if j==w[:len(j)]:
                    words[ind]=j
                    break
        return " ".join(words)
