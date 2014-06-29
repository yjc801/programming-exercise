class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    if (l1 == None): return l2
    if (l2 == None): return l1
    dummy = Node(0)
    p = dummy
    while (l1 and l2):
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next
    p.next = l2 if l2 else l1
    return dummy.next

def printList(l):
    array = []
    while l:
        array.append(l.val)
        l = l.next
    print array

if __name__ == '__main__':
    l1 = Node(1)
    l1.next = Node(2)
    l1.next.next = Node(4)
    l2 = Node(3)
    printList(mergeTwoLists(l1,l2))