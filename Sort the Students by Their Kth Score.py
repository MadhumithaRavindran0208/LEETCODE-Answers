class Solution(object):
    def sortTheStudents(self, score, k):
        sorted1=[]
        for i in range(len(score)):
            sorted1.append((score[i][k],i))
        sorted1=sorted(sorted1,reverse=True)
        result=[]
        for i,j in sorted1:
            result.append(score[j])
        return result
class Solution(object):
    def sortTheStudents(self, score, k):
        return sorted(score,key=lambda x:x[k],reverse=True)