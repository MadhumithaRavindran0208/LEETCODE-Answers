class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        def proper(s):
            s=s.replace("i","")
            n=s.split("+")
            return int(n[0]),int(n[1])
        a,b=proper(num1)
        c,d=proper(num2)
        r=(a*c)-(b*d)
        i=(b*c)+(d*a)
        return str(r)+"+"+str(i)+"i"