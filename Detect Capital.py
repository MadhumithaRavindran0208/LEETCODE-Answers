class Solution(object):
    def detectCapitalUse(self, word):
        return word.istitle() or word.isupper() or word.islower()