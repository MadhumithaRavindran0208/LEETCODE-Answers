class Solution(object):
    def finalValueAfterOperations(self, operations):
        c=0
        for i in operations:
            if "--" in i:c-=1
            if "++" in i:c+=1
        return c
        