class Solution(object):
    def toHex(self, num):
        if num == 0: return "0"
        if num < 0: num = num & 0xFFFFFFFF
        chars = "0123456789abcdef"
        result = ""
        while num > 0:
            result = chars[num % 16] + result
            num //= 16
        return result