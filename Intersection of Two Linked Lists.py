class Solution(object):
    def getIntersectionNode(self, headA, headB):
        listed=set()
        current=headA
        while current:
            listed.add(current)
            current=current.next
        current=headB
        while current:
            if current in listed:
                return current
            current=current.next
          