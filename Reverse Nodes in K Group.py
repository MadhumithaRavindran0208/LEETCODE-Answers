class Solution(object):
    def reverseKGroup(self, head, k):
        h=head
        l=[]
        while h:
            l.append(h.val)
            h=h.next
        n=len(l)
        for i in range (0,n,k):
            if i+k<=n:l[i:i+k]=l[i:i+k][::-1]
        h=head
        for i in l:
            h.val=i
            h=h.next
        return head
        