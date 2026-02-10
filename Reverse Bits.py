class Solution(object):
    def reverseBits(self, n):
        binary=str('{:032b}'.format(n))
        return int(binary[::-1],2)