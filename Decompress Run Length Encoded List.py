class Solution(object):
    def decompressRLElist(self, nums):
        result=[]
        ind=0
        for i in range (0,len(nums)-1,2):
            result[ind:]=[nums[i+1]]*nums[i]
            ind+=nums[i]
        return result