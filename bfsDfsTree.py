class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def dfs_recursive(root):
    if not root:
        return []
    visited_nodes = [root.data]
    visited_nodes.extend(dfs_recursive(root.left))
    visited_nodes.extend(dfs_recursive(root.right))
    return visited_nodes

#     1
#    / \
#   3   5
#  / \   \
# 2   4   6
# bfs = [1, 3, 5, 2, 4, 6]
# nodes_to_visit = [2, 4, 6]
# nodes_visited = [1, 3, 5, 2, 4, 6]
# node = 5
def bfs_iterative(root):
    nodes_to_visit = [root]
    nodes_visited = []
    while nodes_to_visit:
        node = nodes_to_visit.pop(0)
        nodes_visited.append(node.data)
        if node.left: nodes_to_visit.append(node.left)
        if node.right: nodes_to_visit.append(node.right)
    return nodes_visited




# nodes_to_visit = [6]
# visited_nodes = [1, 3, 2, 4, 5, ]
# node = 5
def dfs_iterative(root):
    nodes_to_visit = [root]
    visited_nodes = []
    while nodes_to_visit:
        node = nodes_to_visit.pop(0)
        visited_nodes.append(node.data)
        if node.right: nodes_to_visit.insert(0,node.right)
        if node.left: nodes_to_visit.insert(0,node.left)
    return visited_nodes
 #     1
 #    / \
 #   3   5
 #  / \   \
 # 2   4   6
 # DFS = [1,3,2,4,5,6]
tree = Node(1,
            Node(3,
                 Node(2),
                 Node(4)),
            Node(5,
                 None,
                 Node(6)))

assert dfs_recursive(tree) == [1,3,2,4,5,6]
assert dfs_iterative(tree) == [1,3,2,4,5,6]
assert bfs_iterative(tree) == [1, 3, 5, 2, 4, 6]

