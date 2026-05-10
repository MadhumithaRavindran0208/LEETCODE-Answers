class Solution(object):
    def findDuplicates(self, nums):
        l=[]
        from collections import Counter
        count=Counter(nums)
        for num,f in count.items():
            if f>1:l.append(num)
        return l
class Solution(object):
    def findDuplicates(self, nums):
        l=[]
        for i in set(nums):
            if nums.count(i)>1:l.append(i)
        return l