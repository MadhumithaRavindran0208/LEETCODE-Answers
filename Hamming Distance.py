class Solution(object):
    def hammingDistance(self, x, y):
        x=format(x,"032b")
        y=format(y,"032b")
        c=0
        for i,j in zip(x,y):
            if i!=j:c+=1
        return c
        