class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        c=0
        if max(hours)>=target:
            for i in hours:
                if i>=target:c+=1
        return c