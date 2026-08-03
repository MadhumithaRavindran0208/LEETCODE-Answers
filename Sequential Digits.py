class Solution(object):
    def sequentialDigits(self, low, high):
        l=[]
        for i in range(low,high):
            a=str(i)
            c=0
            for j in range (len(a)-1):
                if int(a[j+1])-int(a[j])==1:c+=1
            if c==len(a)-1:l.append(i)
        return l
class Solution(object):
    def sequentialDigits(self, low, high):
        l=[]
        for length in range(2, 10):
            for start in range(1, 10 - length + 1):
                num = int("".join(str(start + k) for k in range(length)))
                if low <= num <= high:
                    l.append(num)
        return sorted(l)
