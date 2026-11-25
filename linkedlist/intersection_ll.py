# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # two pointer
        lista = headA
        listb = headB
        while lista != listb: #loop continues as long as both pointers point to the same node
            lista = lista.next if lista else headB # we are switching head because the length of the two linkedlists are different and it ensures that both pointers traverse equal distance
            listb = listb.next if listb else headA
        return lista
# TimeComplexity : O(m+n) where m and n are the lengths of both linkedlist
# Space Complexity : O(1) 
        