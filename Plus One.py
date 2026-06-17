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
class Solution(object):
    def plusOne(self, digits):
        digit=""
        for i in digits:
            digit=digit+str(i)
        digit=int(digit)+1
        final=[]
        for i in str(digit):
            final.append(int(i))
        return final
        
