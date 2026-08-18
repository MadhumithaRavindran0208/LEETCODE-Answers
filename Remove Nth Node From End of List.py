class Solution(object):
    def removeNthFromEnd(self, head, n):
        c=1
        original=temp=head
        while head.next:
            c+=1
            head=head.next
        i=0
        if c==n:return temp.next
        while i<c-n-1:
            temp=temp.next
            i+=1
        temp.next=temp.next.next
        head=temp
        return original
        