class Solution(object):
    def totalWaviness(self, num1, num2):
        peaks=0
        for i in range(num1,num2+1):
            a=str(i)            
            if i//100>0 and i//100<10:
                if a[1]>a[0] and a[1]>a[2]:peaks+=1
                if a[1]<a[0] and a[1]<a[2]:peaks+=1
            if i//100>9:
                for j in range(1,len(a)-1):
                    if a[j]>a[j-1] and a[j]>a[j+1]:peaks+=1  
                    elif a[j]<a[j-1] and a[j]<a[j+1]:peaks+=1
        return peaks
        