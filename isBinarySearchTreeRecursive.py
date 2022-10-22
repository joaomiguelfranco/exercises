class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def check_left(node):
    if not node.left: return True
    if node.left.data < node.data:
        return True
    return False


def check_right(node):
    if not node.right: return True
    if node.right.data > node.data:
        return True
    return False

def isBst(root, min, max):
    if not root:
        return True

    if min and root.data <= min: return False
    if max and root.data >= max: return False

    if check_left(root) and check_right(root):
        return isBst(root.left, min, root.data) and \
               isBst(root.right, root.data, max)

def check_binary_search_tree_(root):
    return isBst(root, None, None)


tree = Node(3,
            Node(5,
                 Node(1),
                 Node(4)),
            Node(2,
                 Node(6)))

assert not check_binary_search_tree_(tree)
#      5
#     / \
#    /   \
#   3     7
#  / \    /
# 1   4  6
tree = Node(5,
            Node(3,
                 Node(1),
                 Node(4)),
            Node(7,
                 Node(6)))
assert check_binary_search_tree_(tree)
#       3
#     /   \
#    /     \
#   2       6
#  / \     / \
# 1   4   5   7
tree = Node(3,
            Node(2,
                 Node(1),
                 Node(4)),
            Node(6,
                 Node(5),
                 Node(7)))
assert not check_binary_search_tree_(tree)

tree = Node(3,
            Node(2,
                 Node(1),
                 Node(3)),
            Node(6,
                 Node(5),
                 Node(7)))

