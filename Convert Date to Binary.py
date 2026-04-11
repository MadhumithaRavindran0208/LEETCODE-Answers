class Solution(object):
    def convertDateToBinary(self, date):
        l=date.split("-")
        return "-".join(bin(int(i))[2:]for i in l)
            
        