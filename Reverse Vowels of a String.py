class Solution(object):
    def reverseVowels(self, s):
        c = list(s)
        v = set("aeiouAEIOU")
        left, right = 0, len(c) - 1
        while left < right:
            while left < right and c[left] not in v:
                left += 1
            while left < right and c[right] not in v:
                right -= 1
            c[left], c[right] = c[right], c[left]
            left += 1
            right -= 1  
        return "".join(c)