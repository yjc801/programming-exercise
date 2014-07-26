class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseBetween(head, m, n):
    if head == None or head.next == None:
        return head
    counter = m
    
    dummy_head = ListNode(0)
    dummy_head.next = head
    p = dummy_head

    while counter:
        p = p.next
        counter-=1
    prev = p
    p = p.next
    prev.next = reverseList(p,n-m+1)
    return dummy_head.next

def reverseList(head,counter):
    prev, curr = None, head
    while counter:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        counter-=1
    head.next, head = curr, prev
    return head

def reverseRec(head):
    if not head:
        return
    p = head.next
    if not p:
        return
    reverseRec(p)
    p.next = head
    head.next = None
    # how to fix head?

def reverseBetween2(head, m, n):
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

def reverse(root):
    prev, curr = None, root
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def move(root,k):
    while k:
        root, k = root.next, k-1
    print root.val

def printList(head):
    p = head
    count = 5
    while count:
        print p.val
        p=p.next
        count-=1

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
    move(head,2)
    # printList(head)