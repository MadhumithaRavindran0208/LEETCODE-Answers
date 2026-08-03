
class Solution(object):
    def isPalindrome(self, head):
        current=head
        a=[]
        while current:
            a.append(current.val)
            current=current.next
        for i in range (len(a)/2+1):
            if a[i]!=a[(i*-1)-1]:return False 
        return True