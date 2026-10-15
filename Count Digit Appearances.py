class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        a=0
        for i in nums:
            a+=str(i).count(str(digit))
        return a
class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        a=0
        nums="".join(str(nums))
        digit=str(digit)
        for i in nums:
            if i==digit:a+=1
        return a
class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        nums="".join(str(nums))
        
        return nums.count(str(digit))
class Solution(object):
    def countDigitOccurrences(self, nums, digit):        
        return str(nums).count(str(digit))
       