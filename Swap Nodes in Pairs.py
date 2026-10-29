class Solution(object):
    def swapPairs(self, head):
        c=[]
        h=head
        while h:
            c.append(h.val)
            h=h.next
        for i in range (0,len(c)-1,2):
            c[i],c[i+1]=c[i+1],c[i]
        h=head
        for i in c:
            h.val=i
            h=h.next
        return head      