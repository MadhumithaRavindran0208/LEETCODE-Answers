class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        d={}
        for i in arr1:
            d[i]=d.get(i,0)+1
        r=[]
        for i in arr2:
            if i in arr1:
                r.extend([i]*d[i])
        arr=[]
        for i in arr1:
            if i not in arr2:
                arr.append(i)
        arr.sort()
        return r+arr