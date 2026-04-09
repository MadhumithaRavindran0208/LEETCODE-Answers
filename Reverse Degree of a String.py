class Solution(object):
    def reverseDegree(self, s):
        sum1=0
        al=['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
        for i in (s):
            sum1+=(s.index(i)+1)*(al.index(i)+1)
        return(sum1)
class Solution(object):
    def reverseDegree(self, s):
        sum1=0      
        for i in range (len(s)):
            sum1+=(i+1)*abs(ord(s[i])-123)
        return(sum1)