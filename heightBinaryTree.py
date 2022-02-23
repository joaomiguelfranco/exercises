class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# root = 4
# q [(0,4)]
# maxheight
# level = 0
# curNode = 4
# q = [(1,6),(1,2)]
# level = 1
# curnode = 2
# maxHeight = 1
# q = [(1,2),(2,3),(2,1)]
def getHeightTree(root):
    maxHeight = 0
    # bfs -> q
    q = [(0,root)]
    while q:
        level,curNode = q.pop()
        if level > maxHeight:
            maxHeight = level
        if curNode.right: q.append((level + 1, curNode.right))
        if curNode.left: q.append((level + 1, curNode.left))

    return maxHeight

#       4
#     /   \
#    2     6
#   / \   / \
#  1   3 5   7
# /
#0
tree = Node(4,
            Node(2,
                 Node(1,
                      Node(0)),
                 Node(3)),
            Node(6,
                 Node(5),
                 Node(7)))
assert 3 == getHeightTree(tree)

#      4
tree = Node(4)
assert 0 == getHeightTree(tree)

#      4
#    /   \
#   2     6
#  / \   / \
# 1   3 5   7
tree = Node(4,
            Node(2,
                 Node(1),
                 Node(3)),
            Node(6,
                 Node(5),
                 Node(7)))
assert 2 == getHeightTree(tree)

#       4
#     /
#    2
#   /
#  1
tree = Node(4,
            Node(2,
                 Node(1)
                 )
            )
assert 2 == getHeightTree(tree)