class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):
        node = Node(val)

        if  not self.root:
            self.root = node
            return

        prev = self.root
        eligible = self.root

        while eligible:
            prev = eligible
            eligible = prev.left if val < prev.info else prev.right

        if val < prev.info:
            prev.left = node
        else: prev.right = node


# Enter you code here.

#        4
#      /   \
#     2     7
#    / \
#   1   3

tree = BinarySearchTree()
tree.insert(4)
tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(3)
tree.insert(6)
preOrder(tree.root)
