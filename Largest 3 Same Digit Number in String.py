class Solution(object):
    def largestGoodInteger(self, num):
        m=""
        for i in range (len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                m=max(num[i],m)
        return m*3
        