import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def insertionSortList(head):
    if not head:
        return None
    dummy = ListNode(-sys.maxint)
    # dummy.next = head
    curr = head
    while curr:
        pos = findPos(dummy,curr.val)
        temp = curr.next
        curr.next = pos.next
        pos.next = curr
        curr = temp
    return dummy.next
        
    
def findPos(head,val):
    prev = None
    curr = head
    while curr and curr.val <= val:
        prev = curr
        curr = curr.next
    return prev

def printList(head):
    p = head
    while p:
        print "%s" % p.val
        p=p.next


if __name__ == '__main__':
    head = ListNode(5)
    head.next = ListNode(2)
    head.next.next = ListNode(3) 
    head.next.next.next = ListNode(1)
    head.next.next.next.next = ListNode(0)
    # printList(head)
    head = insertionSortList(head)
    printList(head)