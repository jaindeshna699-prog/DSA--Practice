# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next: # this ensures that fast and fast.next are valid before moving 2 steps
            fast = fast.next.next
            slow = slow.next
            if slow == fast: # cycle detected
                return True
        return False
# Time complexity : O(N) no. of nodes before the cycle + no.of nodes in the cycle
# Space Complexity : O(1)
            
        