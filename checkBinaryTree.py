class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBinaryTree(node):
    q = [node]
    while q:
        curNode = q.pop(0)
        if curNode.left:
            if curNode.val <= curNode.left.val:
                return False
            q.append(curNode.left)
        if curNode.right:
            if curNode.val >= curNode.right.val:
                return False
            q.append(curNode.right)
    return True

#     6
#    / \
#   4   8
#  / \
# 2   5
tree = Node(6,
            Node(4,
                 Node(2),
                 Node(5)
                 ),
            Node(8)
            )
assert isBinaryTree(tree)


#     6
#    / \
#   4   8
#  / \
# 2   3
tree = Node(6,
            Node(4,
                 Node(2),
                 Node(3)
                 ),
            Node(8)
            )
assert not isBinaryTree(tree)


#     6
#    /
#   4
#  /
# 2
tree = Node(6,
            Node(4,
                 Node(2)
                 ),
            )
assert isBinaryTree(tree)

#     6
tree = Node(6)
assert isBinaryTree(tree)

#     6
#    / \
#   4   8
#  / \   \
# 2   5   9
tree = Node(6,
            Node(4,
                 Node(2),
                 Node(5)
                 ),
            Node(8,
                 None,
                 Node(9))
            )
assert isBinaryTree(tree)