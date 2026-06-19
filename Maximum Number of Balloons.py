class Solution(object):
    def maxNumberOfBalloons(self, text):
        from collections import Counter
        count=Counter(text)
        return min(count["b"],count["a"],count["l"]/2,count["o"]/2,count["n"])
        