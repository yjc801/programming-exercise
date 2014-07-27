class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseBetween(head, m, n):
    dummy = ListNode(0)
    dummy.next = head
    prev, curr = None, dummy
    count = m
    while count:
        prev, curr = curr, curr.next
        count-=1

    before_start = prev
    start = curr
    count  = n - m + 1
    while count:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        count -= 1

    before_start.next = prev
    start.next = curr

    return dummy.next

def reverseKGroup(head, k):
    dummy = ListNode(-1)
    dummy.next = head
    prev, curr = dummy, head
    while curr:
        p = curr
        count = k
        while p and count-1:
            p, count = p.next, count-1
        if not p:
            break
        prev, curr = curr, reverseList(prev, curr, k)
    return dummy.next

def reverseList(before_start, head,counter):
    prev, curr = None, head
    while counter:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        counter-=1
    head.next, head = curr, prev
    before_start.next = head
    return curr

def printList(head):
    p = head
    count = 5
    while count:
        print p.val
        p=p.next
        count-=1

# Basics
def reverse(root):
    ''' Reverse whole list
    '''
    prev, curr = None, root
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def move(root,k):
    ''' move k steps, return the k+1 th node 
    '''
    while k:
        root, k = root.next, k-1
    print root.val
    return root


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3) 
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # head = reverseRec(head)
    # printList(head)
    # counter = 2
    # head = reverseList(head,counter)
    # head = reverseBetween2(head,1,2)
    # head = reverse(head)
    # move(head,2)
    head = reverseKGroup(head,4)
    printList(head)
