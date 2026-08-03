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
        