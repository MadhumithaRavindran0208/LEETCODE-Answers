class Solution(object):
    def addDigits(self, num):
        while num>9:
            a=0
            for i in str(num):
                a+=int(i)
            num=a
        return (num)


        