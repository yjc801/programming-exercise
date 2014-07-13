class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sumNumbers(root):
	return helper(root,"")
    
def helper(node,path):
	if not node:
		return 0
	path += str(node.val)
	if not node.left and not node.right:
		return int(path)
	return helper(node.left,path) + helper(node.right,path)

if __name__ == '__main__':
	node = TreeNode(1)
	node.left = TreeNode(2)
	node.right = TreeNode(3)
	node.right.right = TreeNode(4)
	print sumNumbers(node)