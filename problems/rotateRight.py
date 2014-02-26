# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None or k == 0: return head

        runner = head
        chaser = head
        
        while(k > 0):
            k = k-1
            if runner == None: runner = head
            runner = runner.next
        
        if runner == None: return head
        
        while(runner.next):
            runner = runner.next
            chaser = chaser.next
        
        runner.next = head
        head = chaser.next
        chaser.next = None
        
        return head