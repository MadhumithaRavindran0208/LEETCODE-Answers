class Solution(object):
    def createTargetArray(self, nums, index):
        n=len(nums)
        result=[0]
        for i,j in zip(nums,index):
            a=result[j:]
            result[j]=i
            result[j+1:]=a
        return result[:n]
class Solution(object):
    def createTargetArray(self, nums, index):
        result=[]
        for i,j in zip(nums,index):
            result.insert(j,i)
        return result