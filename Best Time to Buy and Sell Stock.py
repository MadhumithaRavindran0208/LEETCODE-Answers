class Solution(object):
    def maxProfit(self, prices):
        min_p= float('inf')
        max_p= 0
        for i in prices:
            if i < min_p:
                min_p = i
            elif i - min_p > max_p:
                max_p = i - min_p
        return max_p
        