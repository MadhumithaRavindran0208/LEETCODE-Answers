class Solution(object):
    def reverseBetween(self, head, left, right):
        l,r=1,left
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while l<left:
            prev=prev.next
            l+=1
        arr=prev.next
        while r<right:
            next_node=arr.next
            arr.next=next_node.next
            next_node.next=prev.next
            prev.next=next_node
            r+=1
        return dummy.next