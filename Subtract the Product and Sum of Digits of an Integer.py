class Solution(object):
    def subtractProductAndSum(self, n):
        m=1
        a=0
        for i in str(n):
            m*=int(i)
            a+=int(i)
        return m-a