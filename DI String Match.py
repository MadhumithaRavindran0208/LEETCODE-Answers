class Solution(object):
    def diStringMatch(self, s):
        length,low=len(s),0
        result=[]
        for i in range (length):
            if s[i]=="D":
                result.append(length)
                length-=1
            else:
                result.append(low)
                low+=1
        result.append(low)
        return result
