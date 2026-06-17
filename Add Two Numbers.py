
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10 
            val = val % 10   
            current.next = ListNode(val)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l11=l1
        l22=l2
        num1=[]
        num2=[]
        while l11:
            num1.append(l11.val)
            l11=l11.next
        while l22:
            num2.append(l22.val)
            l22=l22.next
        num1=num1[::-1]
        num2=num2[::-1]
        num11=0
        num22=0
        for i in range(len(num1)):
            num11=num11*10+num1[i]
        for i in range(len(num2)): 
            num22=num22*10+num2[i]
        num11+=num22
        dummy=ListNode(0)
        d=dummy
        for i in str(num11)[::-1]:
            d.next=ListNode(int(i))
            d=d.next
        return dummy.next
