class Solution(object):
    def largestOddNumber(self, num):
        if int(num)%2==1:return num
        else:
            for i in range (len(num)-1,-1,-1):
                if int(num[i])%2==1:return num[:i+1]
            else:return ""
class Solution(object):
    def largestOddNumber(self, num):
        return num.rstrip("02468")
     