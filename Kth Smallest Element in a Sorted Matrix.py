class Solution(object):
    def kthSmallest(self, matrix, k):
        l=[]
        for i in matrix:
            for j in i:l.append(j)
        l.sort()
        return l[k-1]
        