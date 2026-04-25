class Solution(object):
    def maximumWealth(self, accounts):
        maxi=0
        for i in accounts:
            maxi=max(sum(i),maxi)
        return maxi
        