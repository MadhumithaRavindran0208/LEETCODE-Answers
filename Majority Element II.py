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