class Solution(object):
    def hammingWeight(self, n):
        a=str(bin(n))
        c=0
        for i in a:
            if i=="1":
                c+=1
        return (c)
        