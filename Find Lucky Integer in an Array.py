class Solution(object):
    def findLucky(self, arr):
        n=-1
        for i in set(arr):
            if arr.count(i)==i:n=max(i,n)
        return n
class Solution(object):
    def findLucky(self, arr):
        n=-1
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i]==i:n=max(i,n)
        return n
        