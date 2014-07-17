import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def zigzagLevelOrder(root):
    if not root:
        return []
    curr, next, temp, res = collections.deque(), collections.deque(), [], []
    curr.append(root)
    reverse = False
    while curr:
        while curr:
            node = curr.popleft()
            if node:
                temp.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
        if reverse:
            temp.reverse()
        res.append(temp)
        reverse = not reverse
        curr, next = next, curr
        temp = []
    return res

if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    # node.left.left = TreeNode(4)
    # node.right.right = TreeNode(5)
    print zigzagLevelOrder(node)