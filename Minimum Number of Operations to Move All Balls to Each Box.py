class Solution(object):
    def minOperations(self, boxes):
        box=list(boxes)
        n=len(box)
        result=[0]*n
        ones=[]
        for i in range(n):
            if box[i]=="1":ones.append(i)
        for i in range(n):
            for j in ones:
                result[i]+=abs(i-j)
        return result