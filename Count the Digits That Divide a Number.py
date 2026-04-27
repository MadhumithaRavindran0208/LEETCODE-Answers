class Solution(object):
    def countDigits(self, num):
        c=0
        for i in str(num):
            if num%int(i)==0:c+=1
        return c
        