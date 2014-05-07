def copyRandomList(head):
    if head == None:
        return head
    
    p = head
    while p:
        temp = RandomListNode(p.label)
        temp.next = p.next
        p.next =temp
        p = temp.next

    p = head
    while p:
        if p.random:
            p.next.random = p.random.next
        p = p.next.next

    p = head
    new_head = head.next
    while p and p.next:
        temp = p.next
        p.next = temp.next
        p = temp    
    return new_head