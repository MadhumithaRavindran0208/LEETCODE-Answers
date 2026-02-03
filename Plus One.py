class Solution(object):
    def plusOne(self, digits):
        a=0
        for i in range (len(digits)):
            a=a*10
            a+=digits[i]
        a+=1
        list_a=[]
        for i in (str(a)):
            list_a.append(int(i))
        return(list_a)
        