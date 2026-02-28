class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        no=set(nums)
        d={}
        for i in no:
            n=0
            for j in nums:
                if i==j:
                    n+=1
            d[i]=n
        for i in no:
            if d[i]==max(d.values()):
                return(i)