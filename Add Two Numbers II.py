class Solution(object):
    def addTwoNumbers(self, l1, l2):
        list1=[]
        while l1:
            list1.append(str(l1.val))
            l1=l1.next
        list1=int("".join(list1))
        list2=[]
        while l2:
            list2.append(str(l2.val))
            l2=l2.next
        list2=int("".join(list2))
        list1+=list2
        dummy=ListNode(0)
        d=dummy
        for i in str(list1):
            d.next=ListNode(int(i))
            d=d.next
        return dummy.next
        