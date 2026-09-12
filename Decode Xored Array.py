class Solution(object):
    def decode(self, encoded, first):
        n=len(encoded)
        result=[0]*(n+1)
        result[0]=first
        for i in range (1,n+1):
            result[i]=result[i-1]^encoded[i-1]
        return result
            