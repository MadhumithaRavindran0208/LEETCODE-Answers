class Solution(object):
    def bitwiseComplement(self, n):
        n=bin(n)[2:]
        n1=""
        for i in str(n):
            if i=="0":n1+="1"
            else:n1+="0"
        return int(n1,2)