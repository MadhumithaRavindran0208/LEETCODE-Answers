class Solution(object):
    def checkPerfectNumber(self, num):
        if num<=1:return (bool(0))
        c=1
        for i in range (2,int(num**0.5)+1):
            if num%i==0:
                c+=i
                if i*i!=num:
                    c+=num/i
        return (c==num)