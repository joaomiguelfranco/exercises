# NOT COMPLETE. THIS EXERCISE NEEDS LEFT-RIGHT & RIGHT-LEFT ROTATION
# uncomment the last line of this file to unleash the issue :)

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

    def height(self, root):
        if not root:
            return 0

        q = [root]
        maxHeight = 0
        while q:
            node = q.pop(0)
            maxHeight = max(maxHeight, node.level)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return maxHeight

    def getMinNode(self, root):
        q = [root]
        minNode = root
        while q:
            node = q.pop(0)
            if node.info < minNode.info:
                minNode = node
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return minNode

    def getMaxNode(self, root):
        q = [root]
        maxNode = root
        while q:
            node = q.pop(0)
            if node.info > maxNode.info:
                maxNode = node
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return maxNode

    def detachNode(self, root, nodeToBeDetached):
        q = [root]
        while q:
            node = q.pop(0)
            if node.left == nodeToBeDetached:
                node.left = None
                return
            elif node.right == nodeToBeDetached:
                node.right = None
                return
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

    def recalculateLevels(self, root):
        q = [root]
        root.level = 0
        while q:
            node = q.pop(0)
            if node.left:
                node.left.level = node.level + 1
                q.append(node.left)
            if node.right:
                node.right.level = node.level + 1
                q.append(node.right)




    def rightRotation(self, root):
        if not root:
            return

        rightNode = self.getMinNode(root.right)
        self.detachNode(root.right, rightNode)
        tmp = root
        tmp.right = None
        self.root = rightNode
        self.root.left = tmp


    def leftRotation(self, root):
        if not root:
            return

        leftNode = self.getMaxNode(root.left)
        self.detachNode(root.right, leftNode)
        tmp = root
        tmp.left = None
        root = leftNode
        root.right = tmp

    def balanceTree(self):
        leftHeight = self.height(self.root.left)
        rightHeight = self.height(self.root.right)
        balanceFactor = leftHeight - rightHeight
        if balanceFactor < -1:
            self.rightRotation(self.root)
        elif balanceFactor > 1:
            self.leftRotation(self.root)
        self.recalculateLevels(self.root)
        print(f"node {self.root.info} balance={balanceFactor} leftHeight={leftHeight} rightHeight={rightHeight}")

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):
        node = Node(val)

        if  not self.root:
            self.root = node
            self.root.level = 0
            return

        prev = self.root
        eligible = self.root

        while eligible:
            prev = eligible
            eligible = prev.left if val < prev.info else prev.right

        node.level = prev.level + 1
        if val < prev.info:
            prev.left = node
        else: prev.right = node

        self.balanceTree()


# Enter you code here.



#        3
#      /   \
#     2     4
#            \
#             5
# ADD 6
#        4
#      /   \
#     3     5
#    /       \
#   2         6
tree = BinarySearchTree()
tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(5)
assert 3 == tree.root.info
tree.insert(6)
assert 4 == tree.root.info


tree = BinarySearchTree()
tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
assert 5 == tree.root.info



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

assert 4 == tree.root.info



tree = BinarySearchTree()
tree.insert(5)
tree.insert(7)
tree.insert(6)
assert 6 == tree.root.info
# assert 7 == tree.root.right.info