class Solution(object):
    def partition(self, head, x):
        less=[]
        great=[]
        hh=head
        n=0
        dummy=ListNode(0)
        d=dummy
        while hh:
            if hh.val<x:less.append(hh.val)
            else:great.append(hh.val)
            hh=hh.next
        l=less+great
        for i in l:
            dummy.next=ListNode(i)
            dummy=dummy.next
        return d.next