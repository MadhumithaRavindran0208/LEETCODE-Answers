class Solution(object):
    def removeDuplicates(self, s):
        s=list(s)
        i=1
        while i<len(s):
            if s[i]==s[i-1]:
                del s[i]
                del s[i-1]
                i=max(1,i-1)
            else:i+=1
        return "".join(s)
class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for i in s:
            if stack and stack[-1]==i:
                stack.pop()
            else:stack.append(i)
        return "".join(stack)