class Solution(object):
    def customSortString(self, order, s):
        l1=[]
        l2=[]
        for i in order:
            if i in s:l1.append(i*s.count(i))
        for i in sorted(set(s)):
            if i not in order:l2.append(i*s.count(i))
        l1+=l2
        return "".join(l1)