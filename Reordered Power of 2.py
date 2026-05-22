class Solution(object):
    def reorderedPowerOf2(self, n):
        for i in range (31):
            if sorted(list(str(2**i)))==sorted(list(str(n))):return True  
        else:return False