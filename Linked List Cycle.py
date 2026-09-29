class Solution(object):
    def hasCycle(self, head):
        seen = set()
        current = head
        while current:
            if current in seen: 
                return True
            seen.add(current)
            current = current.next
        return False
class Solution(object):
    def hasCycle(self, head):
        l=[-1]
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next          
            fast=fast.next.next     
            if slow==fast:         
                return True 
        return False     
