# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        temp = head #1
        while temp:
            front = temp.next #2
            temp.next = prev #1->None
            prev = temp #1
            temp = front #2
        return prev




            
        