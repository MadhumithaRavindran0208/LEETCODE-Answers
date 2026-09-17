class Solution(object):
    def getSneakyNumbers(self, nums):
        d={}
        result=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i]==2:result.append(i)
        return result
        