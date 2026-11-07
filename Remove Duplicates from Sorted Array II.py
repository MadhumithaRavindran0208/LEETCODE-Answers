class Solution(object):
    def removeDuplicates(self, nums):
        d={}
        c=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in sorted(d):
            if d[i]>=2:
                c.append(i)
                c.append(i)
            if d[i]==1:
                c.append(i)
        nums[:]=c[:]
        return len(c)
