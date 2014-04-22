# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None: return head
        chaser = head
        runner = head.next
        while(runner):
            if chaser.val == runner.val:
                chaser.next = runner.next
                runner = chaser.next
            else:
                chaser = chaser.next
                runner = runner.next
        return head
