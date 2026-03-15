class Solution(object):
    def countDigitOne(self, n):
        count=0
        factor = 1
        while factor <= n:
            divider = factor * 10
            count += (n // divider) * factor
            count += min(max(n % divider - factor + 1, 0), factor)
            factor *= 10
        return (count)
    def countDigitOne(self,n):
        count=0
        for i in range(n+1):
            s=list(str(i))
            for k in s:
                if k=="1":
                    count+=1
        return (count)
    def countDigitOne(self,n):
        count=0
        for i in range(n+1):
            count+=str(i).count("1")
        return (count)
print(Solution().countDigitOne(13))