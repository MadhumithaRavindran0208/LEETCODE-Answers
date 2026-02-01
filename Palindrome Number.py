class Solution(object):
    def isPalindrome(self, x):
        a=str(x)
        rev=a[::-1]
        return (a==rev)