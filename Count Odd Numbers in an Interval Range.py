class Solution(object):
    def countOdds(self, low, high):
        if high%2==1 or low%2==1:return (high-low)//2+1
        else:return (high-low)//2