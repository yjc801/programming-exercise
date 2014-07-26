# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        
        prev, curr = dummy, head
        
        while curr and curr.next:
            next = curr.next
            prev.next = next
            curr.next = next.next
            next.next = curr
            prev = curr
            curr = curr.next
            
        return dummy.next