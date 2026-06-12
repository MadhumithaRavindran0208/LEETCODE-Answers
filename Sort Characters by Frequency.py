class Solution(object):
    def frequencySort(self, s):
        c=[]
        for i in set(s):
            c.append(s.count(i))
        a=sorted(zip(c,set(s)))
        result=[]
        for i,j in a :
            result.append(j*i)
        return "".join(result)[::-1]
        