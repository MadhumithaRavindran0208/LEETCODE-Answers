class Solution(object):
    def findComplement(self, num):
        result=[]
        for i in bin(num)[2:]:
            if i=="0":result.append("1")
            else:result.append("0") 
        return int("".join(result),2)
        