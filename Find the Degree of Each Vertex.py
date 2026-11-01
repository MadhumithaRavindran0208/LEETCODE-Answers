class Solution(object):
    def findDegrees(self, matrix):
        l=[0]*len(matrix)
        for i in range (len(matrix)):
            l[i]=matrix[i].count(1) 
        return l           
class Solution(object):
    def findDegrees(self, matrix):
        l=[]
        for i in matrix:
            l.append(sum(i))
        return l           
