class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lca_bst(root, n1, n2):
    ''' LCA in BST
    '''
    if not root:
        return
    if root.val > n1 and root.val > n2:
        return lca(root.left, n1, n2)
    if root.val < n1 and root.val < n2:
        return lca(root.right, n1, n2)
    return root.val

def lca(root, n1, n2):
    if not root:
        return
    if root.val in (n1, n2):
        return root.val
    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)
    if left and right:
        return root.val
    return left if left else right


if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.right.right = TreeNode(4)

    print lca(node,2,3)