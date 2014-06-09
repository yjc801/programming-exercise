class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def partition(head, x):
    if not head:
        return None
    left_dummy = ListNode(-1)
    right_dummy = ListNode(-1)
    left = left_dummy
    right = right_dummy
    p = head
    while p:
        if p.val < x:
            left.next = p
            left = p
        else:
            right.next = p
            right = p
        p = p.next
    left.next = right_dummy.next
    right.next = None
    return left_dummy.next

def printList(head):
    p = head
    while p:
        print p.val
        p=p.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(5) 
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(0)

    # printList(head)
    # counter = 2
    # head = reverseList(head,counter)
    p = partition(head,3)
    printList(p)