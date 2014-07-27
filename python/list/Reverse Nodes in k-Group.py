# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self,head, k):
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, head
        while curr:
            p, count = curr, k
            while p and count-1:
                p, count = p.next, count-1
            if not p:
                break
            prev, curr = curr, self.reverse(prev, curr, k)
        return dummy.next
    
    def reverse(self,before,head,counter):
        prev, curr = None, head
        while counter:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            counter-=1
        head.next, head = curr, prev
        before.next = prev
        return curr
