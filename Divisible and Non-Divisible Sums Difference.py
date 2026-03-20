class Solution(object):
    def differenceOfSums(self, n, m):
        sum1=sum2=0
        for i in range (n+1):
            if i%m==0:
                sum1+=i
            else:
                sum2+=i
        return (sum2-sum1)
class Solution(object):
    def differenceOfSums(self, n, m):
        l1=[]
        l2=[]
        for i in range (n+1):
            if i%m==0:
                l1.append(i)
            else:
                l2.append(i)
        return (sum(l2)-sum(l1))
        