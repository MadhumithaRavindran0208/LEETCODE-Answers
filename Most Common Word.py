class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        import re
        l = {}
        banned = set(banned)
        words = re.sub(r'[^a-zA-Z ]', ' ', paragraph).lower().split()
        for word in words:
            if word not in banned:
                l[word] = l.get(word, 0) + 1
        return max(l, key=l.get)
        