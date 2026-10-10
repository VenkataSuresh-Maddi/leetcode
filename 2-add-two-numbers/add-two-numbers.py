class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        ans = ""
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            summ = n1 + n2 + carry
            ans = ans+str(summ%10)
            carry = summ//10
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next
        curr = ListNode(int(ans[0]))
        dup = curr
        for i in range(1,len(ans)):
            node = ListNode(int(ans[i]))
            curr.next = node 
            curr = curr.next
        curr.next = None
        return dup