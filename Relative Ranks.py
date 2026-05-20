class Solution(object):
    def findRelativeRanks(self, score):
        l=list(score)
        n=0
        for i in sorted(score,reverse=True):
            if n==0:l[score.index(i)]="Gold Medal"
            elif n==1:l[score.index(i)]="Silver Medal"
            elif n==2:l[score.index(i)]="Bronze Medal"
            else :l[score.index(i)]=str(n+1)
            n+=1
        return l