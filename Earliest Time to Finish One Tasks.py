class Solution(object):
    def earliestTime(self, tasks):
        mini=float("inf")
        for i,j in tasks:
            mini=min(i+j,mini)
        return mini