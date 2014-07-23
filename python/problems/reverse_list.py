class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseBetween(head, m, n):
    if head == None or head.next == None:
        return head
    counter = 1
    
    dummy_head = ListNode(0)
    dummy_head.next = head

    p = dummy_head
    while counter < m:
        p = p.next
        counter+=1
    prev = p
    p = p.next
    prev.next = reverseList(p,n-m+1)
    return dummy_head.next

def reverseList(head,counter):
    p = head
    p_prev = None
    while counter > 0:
        p_next = p.next
        p.next = p_prev
        p_prev = p
        p = p_next
        counter-=1
    head.next = p
    head = p_prev
    return head

def printList(head):
    p = head
    while p:
        print p.val
        p=p.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3) 
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # printList(head)
    # counter = 2
    # head = reverseList(head,counter)
    head = reverseBetween(head,1,3)
    printList(head)


    