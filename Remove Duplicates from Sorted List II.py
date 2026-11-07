class Solution(object):
    def deleteDuplicates(self, head):
        h=head
        d={}
        while h:
            d[h.val]=d.get(h.val,0)+1
            h=h.next
        dummy=ListNode(0)
        dd=dummy
        for i in sorted(d):
            if d[i]==1:
                dd.next=ListNode(i)
                dd=dd.next
        return dummy.next
        