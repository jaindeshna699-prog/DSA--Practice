# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            carry = sum_val // 10
            digit = sum_val % 10

            curr.next = ListNode(digit)
            curr = curr.next
        return dummy.next
# dummy helps us construct the linked list easily, and dummy.next gives us the actual result without the extra dummy node.
# Time complexity = O(max(n,m)) where n and m are the length of l1 and l2 respectively
# Space complexity = O(max(n,m)) because we are returning the linkedlist
# Auxilary space = O(1) (curr,dummy,digit and carry) it is basically extra memory used excluding the input

