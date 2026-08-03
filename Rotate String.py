class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):return False
        for i in range(len(s)):
            a=s[i]
            ind=0
            for j in range (1,len(s)):
                ind=(i+j)%len(s)
                a+=s[ind]
            if a==goal:return True
        return False
class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):return False
        ss=s+s
        return goal in ss
        
        