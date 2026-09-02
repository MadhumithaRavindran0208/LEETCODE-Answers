class Solution(object):
    def rearrangeArray(self, nums):
        positive=[]
        negative=[]
        result=[]
        for i in nums:
            if i<0:negative.append(i)
            else:positive.append(i)
        for i in range (len(nums)//2):
            result.append(positive[i])
            result.append(negative[i])
        return result