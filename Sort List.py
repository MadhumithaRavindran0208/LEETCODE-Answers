class Solution(object):
    def sortList(self, head):
        a=[]
        current=head
        while current:
            a.append(current.val)
            current=current.next
        a.sort()
        current=head
        for i in a:
            current.val=i
            current=current.next
        return head         
        