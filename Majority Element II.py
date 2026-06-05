class Solution(object):
    def majorityElement(self, nums):
        from collections import Counter
        l=[]
        n=len(nums)/3
        count=Counter(nums)
        for num,f in count.items():
            if f>n:l.append(num)
        return l
class Solution(object):
    def majorityElement(self, nums):
        l=[]
        n=len(nums)/3
        for i in set(nums):
            if nums.count(i)>n:l.append(i)
        return l
class Solution(object):
    def majorityElement(self, nums):
        l=[]
        n=len(nums)/3
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in set(nums):
            if d[i]>n:l.append(i)
        return l
