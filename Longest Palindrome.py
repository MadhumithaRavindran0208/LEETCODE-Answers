class Solution(object):
    def longestPalindrome(self, s):
        l=[]
        for i in set(s):
            l.append(s.count(i))
        odd=[]
        even=[]
        n=0
        for i in l:
            if i%2==0:even.append(i)
            else:odd.append(i)
        for i in odd:n+=i-1
        if len(odd)>0:n+=1
        return n+sum(even)