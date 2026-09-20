class Solution(object):
    def numberOfBeams(self, bank):
        light=[]
        for i in bank:
            a=i.count("1")
            if a>0:light.append(a)
        final=0
        for i in range(len(light)-1):
            final+=light[i]*light[i+1]
        return final