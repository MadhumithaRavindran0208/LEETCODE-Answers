class Solution(object):
    def detectCycle(self, head):
        l=set()
        current=head
        while current:
            if current in l:return current
            else:l.add(current)
            current=current.next
        return None
                   