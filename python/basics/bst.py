from collections import deque

class Node:
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None


class BST:
	def __init__(self,sorted_array):
		self.array = sorted_array
		self.root = self.create(0,len(self.array)-1)

	def __repr__(self):
		return "%s"%self.array

	def create(self,low,high):
		if not self.array:
			return None
		if high - low < 0:
			return None
		mid = (low+high)/2
		root = Node(self.array[mid])
		root.left = self.create(low,mid-1)
		root.right = self.create(mid+1,high)
		return root

	def flatten(self,root):
		if not root:
			return
		head = Node(root.val)
		if root.left:
			head.next = Node(self.flatten(root.left).val)
		elif root.right:
			head.next = Node(self.flatten(root.left).val)
		return head

def isBalanced(head): # O(nlogn)
	if not head:
		return True
	def helper(head):
		if not head:
			return 0
		left = helper(head.left)
		right = helper(head.right)
		return max(left,right)+1
	left = helper(head.left)
	right = helper(head.right)
	if abs(left-right) > 1:
		return False
	return isBalanced(head.left) and isBalanced(head.right)

def isBalanced2(head): # O(n)
	if not head:
		return False

	def helper(head):
		if not head:
			return 0
		left = helper(head.left)
		right = helper(head.right)

		if left < 0 or right < 0 or abs(left-right) > 1:
			return -1

		return max(left,right)+1

	return True if helper(head) > 0 else False 


def BFS(head):
	array = [[]]
	queue1 = deque()
	queue1.append(head)
	queue2 = deque()
	while queue1:
		node = queue1.popleft()
		if node:
			array[-1].append(node.val)
			queue2.append(node.left)
			queue2.append(node.right)
		if not queue1 and queue2:
			array.append([])
			queue1,queue2 = queue2,queue1
	return array

def Preorder(head,array):
	if not head:
		return
	array.append(head.val)
	Preorder(head.left,array)
	Preorder(head.right,array)
	return array

def Preorder_iter(head):
	array = []
	stack = []
	node = head
	# stack.append(head)
	while stack or node:
		if node:
			array.append(node.val)
			stack.append(node.right)
			stack.append(node.left)
		node  = stack.pop()
	return array

def Inorder_iter(head):
	array = []
	stack = []
	# stack.append(head)
	node = head
	while stack or node:
		if node:
			stack.append(node)
			node = node.left
		else:
			node = stack.pop()
			array.append(node.val)
			node = node.right
	return array

def Postorder_iter(head):
	array = []
	stack1 = []
	stack2 = []
	stack1.append(head)
	while stack1:
		node = stack1.pop()
		stack2.append(node)
		if node.left:
			stack1.append(node.left)
		if node.right:
			stack1.append(node.right)
	while stack2:
		array.append(stack2.pop().val)
	return array

def Postorder_iter2(head):
	array = []
	stack = []
	# stack.append(head)
	node = head
	prev = None
	while stack or node:
		if node:
			stack.append(node)
			node = node.left
		else:
			top = stack[-1]
			if top.right and prev != top.right:
				node = top.right
			else:
				array.append(top.val)
				prev = top
				stack.pop()
	return array

def Levelorder(head):
	res = []
	level = []
	curr = deque()
	next = deque()
	curr.append(head)
	while curr:
		while curr:
			node = curr.popleft()
			level.append(node.val)
			if node.left:
				next.append(node.left)
			if node.right:
				next.append(node.right)
		res.append(level)
		level = []
		curr,next = next,curr
	return res


def printList(head):
	while head:
		print head.val
		head=head.left

if __name__ == '__main__':
	bst = BST([1,2,3,4,5,6,7])
	root = bst.root
	print root.val
	print "BFS %s" % BFS(root)
	print "Preorder %s" % Preorder(root,[])
	print "Preorder_iter %s" % Preorder_iter(root)
	print "Inorder_iter %s" % Inorder_iter(root)
	print "Postorder_iter %s" % Postorder_iter(root)
	print "Postorder_iter2 %s" % Postorder_iter2(root)
	print "Levelorder %s" % Levelorder(root)
	print "isBalanced %s" % isBalanced(root)
	print "isBalanced %s" % isBalanced2(root)
	# head = bst.flatten(bst.root)
	# print head.next.next.val