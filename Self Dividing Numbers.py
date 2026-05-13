class Solution(object):
    def selfDividingNumbers(self, left, right):
        l=[]
        for i in range (left,right+1):
            a=0
            for j in str(i):
                if j!="0" :
                    if i%int(j)==0:a+=1
            if a==len(str(i)):l.append(i)
        return l
