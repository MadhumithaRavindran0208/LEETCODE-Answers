class Solution(object):
    def balancedStringSplit(self, s):
        c=0
        a=0
        for i in s:
            if i=="R":a+=1
            if i=="L":a-=1
            if a==0:c+=1
        return c