class Solution(object):
    def sortArrayByParityII(self, nums):
        even=[]
        odd=[]
        final=[]
        for i in nums:
            if i%2==0:even.append(i)
            else:odd.append(i)
        for i in range (len(even)):
            final.append(even[i])
            final.append(odd[i])
        return final