# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return None
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        mid = count // 2
        ptr = head
        curr = head
        for i in range(mid + 1):
            ptr = ptr.next
        for i in range(mid-1):
            curr = curr.next
        curr.next = ptr
        return head
# Time complexity = O(N)-> N+N/2+N/2 = 2N
# Space complexity = O(1)

        
        