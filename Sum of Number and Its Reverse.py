class Solution(object):
    def sumOfNumberAndReverse(self, num):
        if num==0:return True
        for i in range (num//2,num):
            a=str(i)[::-1]
            if i+int(a)==num:return True
        else:return False
        