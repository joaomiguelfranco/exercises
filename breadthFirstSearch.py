

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def addNode(self, value):
        if not self.left: self.left = Node(value)
        else : self.right = Node(value)

def findNode(source, root):
    if root.value == source:
        return root
    # BFS we use queue FIFO
    stack = []
    if root.left : stack.append(root.left)
    if root.right : stack.append(root.right)

    while stack:
        elem = stack.pop(0)

        if elem.value == source :
            return elem
        if elem.left : stack.append(elem.left)
        if elem.right :stack.append(elem.right)

def buildTree(edges):
    root = Node(1)
    for edge in edges:
        source = edge[0]
        target = edge[1]
        node = findNode(source, root)
        node.addNode(target)
        print(f"{node.value} -> {target}")
    return root

def bfs(n, m, edges, s):
    """
    calculates the distances to nodes from 's' start node
    :param n: number of nodes
    :param m: number of edges
    :param edges: edges list
    :param s: start node
    :return: distances to nodes from start node
    """
    # build the tree
    tree = buildTree(edges)

    # find the starting node
    node = findNode(s, tree)

    #     1
    #    /  \
    #   2    3
    #       / \
    #      4   5
    #
    # source = 4
    # root = 1
    # stack = [3, None, None]
    # elem = 2

    # for each found node we update result[node-2]
    q = [] #[ (6, 4), (6,5) ]
    if node.left : q.append((6, node.left))
    if node.right: q.append((6, node.right))
    result = []
    for i in range(1, n):
        result.append(-1)
    # [-1, -1, -1] -> 1-2 = -1 | 1-3 = -1
    while q:
        weight, elem = q.pop(0)
        result[elem.value-2] = weight
        if elem.left : q.append((weight + 6, elem.left))
        if elem.right: q.append((weight + 6, elem.right))

    return result



def main():
    res = bfs(5, 3, [[1,2],[1,3],[3,4]], 1)
    print(res)


if __name__ == '__main__':
    main()