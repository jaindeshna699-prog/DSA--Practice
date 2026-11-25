# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        # finding middle by two pointer
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half with middle
        prev = None
        while slow:
            front = slow.next
            slow.next = prev
            prev = slow
            slow = front
        # compare the first and second half
        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
# Time Complexity : O(N)
# Space Complexity : O(1)

        