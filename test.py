# 2. Add Two Numbers
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p, q= l1, l2
        carry = 0
        r = p
        while p and q:
            _sum = p.val + q.val + carry
            p.val = _sum % 10
            carry = _sum / 10
            if not p.next:
                r = p
            p, q = p.next, q.next

        if q:
            r.next = q
            p = q
        while p:
            _sum = p.val + carry
            p.val = _sum % 10
            carry = _sum / 10
            if not p.next:
                r = p
            p = p.next
            if _sum < 10:
                break
        if carry > 0:
            r.next = ListNode(carry)

        return l1

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(0)
        carry = 0
        while l1 or l2:
            val = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry = val / 10
            val %= 10
            p.next = ListNode(val)
            p = p.next
            l1 = l1 and l1.next
            l2 = l2 and l2.next
        if carry > 0:
            p.next = ListNode(carry)
            p = p.next

        return dummy.next
    def helper(self):
        a = []
        for _ in range(1000):
            a.append('*')
        print a[0]
    def add TwoNumber3(self, l1, l2):
        pass
# ---------------------------------------------------------------------- 
