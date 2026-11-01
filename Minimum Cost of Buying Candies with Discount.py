class Solution(object):
    def minimumCost(self, cost):
        final=0
        cost=sorted(cost,reverse=True)
        for i in range(len(cost)):
            if i%3!=2:final+=cost[i]
        return final