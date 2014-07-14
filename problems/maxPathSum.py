class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxPathSum(root):
	max_sum = [-float('inf')]
	helper(root,max_sum)
	return max_sum[0]

def helper(root,max_sum):
	if not root:
		return 0
	left = max(0,helper(root.left,max_sum))
	right = max(0,helper(root.right,max_sum))
	max_sum[0] = max(max_sum[0],left+right+root.val)
	return max(left,right)+root.val

if __name__ == '__main__':
	node = TreeNode(1)
	node.left = TreeNode(2)
	node.right = TreeNode(3)
	node.right.right = TreeNode(-1)
	print maxPathSum(node)