# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        # Add
        curr = head
        while curr:
            new = RandomListNode(curr.label)
            new.next, curr.next = curr.next, new
            curr = curr.next.next
        # Copy
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        # Break
        curr = head
        dummy = RandomListNode(-1)
        p = dummy
        while curr:
            p.next = curr.next
            curr.next = curr.next.next
            p = p.next
            curr = curr.next
        return dummy.next
            
        