class Solution(object):
    def findRestaurant(self, list1, list2):
        list11=[]
        result=[]
        list22={}
        for i,j in enumerate(list2):
            list22[j]=i
        sumu=float("inf")
        for i in range(len(list1)):
            if list1[i] in list2:
                b=list22[list1[i]]
                list11.append((i,b))
                sumu=min(i+b,sumu)
        for i,j in list11:
            if i+j==sumu:result.append(list1[i])
        return result
        