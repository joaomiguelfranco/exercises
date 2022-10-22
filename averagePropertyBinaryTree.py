# '''
# Binary Tree Property Check: Each Node is Average of All Descendents
#
# Given a binary tree check if each node is the average of all its descendants.
# ```
# >>>print_tree(root_1)
#     2 => (2 + 2 + 2+ 1 + 3) / 5 == 2
#    / \
#   2   2 => (1 + 3) / 2 == 2
#  /   / \
# 2   1   3
#
# >>>check_avg_property(root_1)
# True
#
# >>>print_tree(root_2)
#     3 => (2 + 2 + 4 + 3 + 5) = 16, 16 / 5 != 3
#    / \
#   2   4
#  /   / \
# 2   3   5
#
# >>>check_avg_property(root_2)
# False
# ```
#
#       3
#      /
#     3
#    /
#   3
#  /
# 1
# '''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 3
# check_avg(2)
# check_avg(2)
# check_avg(4)
def retrievesElements(root):
    if not root:
        return True
    if not check_avg_property(root):
        return False

    if not retrievesElements(root.right):
        return False
    if not retrievesElements(root.left):
        return False
    return True


#     if root.left:
#         if not check_avg_property(root.left):
#             return False

#     if root.right:
#         if not check_avg_property(root.right):
#             return False
#     return check_avg_property(root)

#     3 => (2 + 2 + 4 + 3 + 5) = 16, 16 / 5 != 3
#    / \
#   2   4
#  /   / \
# 2   3   5

def check_avg_property(root):
    if not root:
        return 0, 0 #n_childs, sum_childs
    l_nchilds,l_sum_childs = check_avg_property(root.left)
    r_nchilds, r_sum_childs = check_avg_property(root.right)

    if


    return

def check_avg_property_not_optimized(root):
    # dfs
    q = [root.left, root.right]
    n_childs = 0
    sum_childs = 0
    #
    while q:
        node = q.pop(0)
        n_childs += 1
        sum_childs += node.val
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return root.val == sum_childs / n_childs



tree = Node(2,
            Node(2,
                 Node(2)
                 ),
            Node(2,
                 Node(1),
                 Node(3)))

assert check_avg_property(tree)

tree = Node(3,
            Node(2,
                 Node(2)
                 ),
            Node(4,
                 Node(3),
                 Node(5)))

assert False == check_avg_property(tree)

tree = Node(2,
            Node(2,
                 Node(2)
                 ),
            Node(1,
                 Node(2),
                 Node(3)))

assert False == check_avg_property(tree)