class Solution(object):
    def rotate(self, matrix):
        mat=zip(*matrix)
        mat1=[]
        for i in mat:
            mat1.append(list(i[::-1]))
        matrix[:]=mat1[:]
        return (matrix)
class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)
        mat=[]
        for i in range(n):
            a=[]
            for j in range(n-1,-1,-1):
                a.append(matrix[j][i])
            mat.append(a)
        for i in range(n):
            matrix[i][:]=mat[i]
        return matrix

