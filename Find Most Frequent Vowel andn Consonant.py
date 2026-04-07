class Solution(object):
    def maxFreqSum(self, s):
        c=0
        max1=max2=0
        for i1 in set(s):
            if i1 in "aeiou":
                max1=max(s.count(i1),max1)
            else:
                max2=max(s.count(i1),max2)
        return(max1+max2)
 