class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
		def Merge(self,l1,l2):
			if (l1 == None): return l2
			if (l2 == None): return l1 
			
			if l1.val > l2.val:
				head = l2
			else:
				head = l1

			l1_prev = ListNode(0)

		while (l1 and l2):
			if (l1.val > l2.val):
				l2_prev = l2
				l2 = l2.next
				l1_prev.next = l2_prev
				l2_prev.next = l1
				l1_prev = l2_prev
			else:
				l1_prev = l1
				l1 = l1.next
		if l2:
			l1_prev.next = l2
		
		return head 

	def Merge_rec(self,l1,l2):
		if l1 == None: return l2
		if l2 == None: return l1
		
		l = ListNode(None)

		if l1.val < l2.val:
			l = l1
			l.next = Merge_rec(l1.next,l2)
		else:
			l = l2
			l.next = Merge_rec(l1,l2.next)
		return l