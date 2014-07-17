class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pathSum(root, sum):
    return helper(root,sum,[],[])

def helper(root,sum,path,res):
    if not root:
        return res
    if not root.left and not root.right and sum == root.val:
        return res+[path+[root.val]]
    return helper(root.left,sum-root.val,path+[root.val],res) + \
           helper(root.right,sum-root.val,path+[root.val],res)


if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.right.right = TreeNode(4)
    print pathSum(node,8)