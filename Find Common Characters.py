class Solution(object):
    def commonChars(self, words):
        l=""
        n=set("".join(words))
        for ch in n:
            a=float("inf")
            for word in words:
                a=min(word.count(ch),a)
            l+=ch*a
        return list(l)
        