class Solution(object):
    def removeElements(self, head, val):
        dummy=ListNode(0)
        dummy.next=head
        h=dummy
        while h.next:
            if h.next.val==val:
                h.next=h.next.next
            else:
                h=h.next
        return dummy.next
        