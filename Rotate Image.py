class Solution(object):
    def rotate(self, matrix):
        mat=zip(*matrix)
        mat1=[]
        for i in mat:
            mat1.append(list(i[::-1]))
        matrix[:]=mat1[:]
        return (matrix)

