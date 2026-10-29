class Solution(object):
    def reorderList(self, head):
        h=head
        hh=[]
        dummy=ListNode(0)
        d=dummy
        while h:
            hh.append(h.val)
            h=h.next
        n=len(hh)
        for i in range(n//2):
            dummy.next=ListNode(hh[i])
            dummy=dummy.next
            dummy.next=ListNode(hh[-(i+1)])
            dummy=dummy.next
        if n%2==1:
            dummy.next=ListNode(hh[n//2])
            dummy=dummy.next
        node=d.next
        head.val=node.val
        head.next=node.next
        return head
