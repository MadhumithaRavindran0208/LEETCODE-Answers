class Solution(object):
    def findNthDigit(self, n):
        l=[]
        for i in range (1,10):
            l.append(i)
        for i in range(10,n+1):
            for j in str(i):l.append(int(j))
            if len(l)>=n:break
        return (l[n-1])
class Solution(object):
    def findNthDigit(self, n):
        d,s = 1,1
        c = 9
        while n > d * c:
            n -= d * c
            d += 1
            c *= 10
            s *= 10
        num = s + (n - 1) // d
        d_index = (n - 1) % d
        return int(str(num)[d_index])