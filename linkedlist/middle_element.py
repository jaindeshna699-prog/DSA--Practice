# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        if head.next is None:
            return head
        count = 0
        temp = head
        
        while temp:
            count += 1
            temp = temp.next
        mid = count // 2
        curr = head
        for i in range(mid):
            curr = curr.next
        return curr

        

        