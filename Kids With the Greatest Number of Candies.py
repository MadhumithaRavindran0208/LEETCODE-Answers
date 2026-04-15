class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        great=[True]*len(candies)
        for i in range (len(candies)):
            if candies[i]+extraCandies>=max(candies):
                continue
            else:
                great[i]=False
        return (great)
        