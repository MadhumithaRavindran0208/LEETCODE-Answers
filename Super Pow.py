class Solution(object):
    def superPow(self, a, b):
        c= "".join(str(i) for i in b)        
        return(pow(a,int(c),1337))
        