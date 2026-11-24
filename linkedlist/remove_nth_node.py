# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # two pointer gap technique
        ptr = head
        temp = head
        for i in range(n): # creates a gap of nodes
            ptr = ptr.next
        if not ptr: # edge case if the removing node is head so if the value of n is the length of linkedlist, pte will point to None
            return head.next
        while ptr.next: # runs until the ptr reaches to the last node
            ptr = ptr.next
            temp = temp.next # now temp has reaches exactly at one node before the removing node
        temp.next = temp.next.next
        return head
# Time complexity = O(L) where l is the length of linkedlist
# Space complexity = O(1)





        