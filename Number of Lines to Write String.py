class Solution(object):
    def numberOfLines(self, widths, s):
        result=[1,0]
        a=0
        for c in s:
            i = widths[ord(c)-ord('a')]
            if a+i<=100:a+=i
            else:
                a=i
                result[0]+=1
        result[1]=a
        return result