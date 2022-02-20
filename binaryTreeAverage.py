"""
Given a binary tree, calculate the average number at each level of the tree

      4
     / \
    7   9
   / \   \
  10  2   6
       \
        6
       /
      2

  Output: [4, 8, 6, 6, 2]
"""

class Node:
    def __init__(self, v, left=None, right=None):
        self.value = v
        self.left = left
        self.right = right

def calculateDepthByDepthFirst(node, depth=0, result={}):
    val = count = 0
    node.depth = depth

    if depth in result:
        val,count = result[depth]
    result[depth] = (val + node.value, count + 1)

    if node.left : calculateDepthByDepthFirst(node.left, depth + 1, result)
    if node.right : calculateDepthByDepthFirst(node.right, depth +1, result)

    return result

def calculateDepthByBreadthFirst(node):
    queue = [(1, node.left), (1,node.right)] # (1,9), (2, 10), (2,2)
    result = {0 : (node.value, 1)}

    while queue:
        curDepth,curNode = queue.pop(0) # 1,7
        if curNode.left : queue.append((curDepth + 1, curNode.left))
        if curNode.right: queue.append((curDepth + 1, curNode.right))

        val = count = 0
        if curDepth in result:
            val,count = result[curDepth]
        result[curDepth] = (val + curNode.value, count + 1)

    return result

def transverseDepthFirstWithRecursion(node):
    if node is None:
        return []

    result = [node]
    result.extend(transverseDepthFirstWithRecursion(node.left))
    result.extend(transverseDepthFirstWithRecursion(node.right))
    return result

def transverseDepthFirst(root):
    result = [root]
    stack = [root.right, root.left]
    while stack:
        curNode = stack.pop()
        if curNode:
            result.append(curNode)
            if (curNode.right): stack.append(curNode.right)
            if (curNode.left): stack.append(curNode.left)
    return result

def transverseBreadthFirst(node):
    result = [node]
    queue = [node.left, node.right]
    while queue:
        curNode = queue.pop(0)
        result.append(curNode)
        if curNode.left : queue.append(curNode.left)
        if curNode.right : queue.append(curNode.right)
    return result

def calculateAveragePerLevel(node, func):
    result = func(node)
    return [val/count for val,count in result.values()]

def buildTree():
    return Node(4,
                Node(7,
                     Node(10),
                     Node(2,
                          Node(6,
                               Node(2)
                               )
                          )
                     ),
                Node(9,
                    None,
                    Node(6)
                     )
                )

def main():
    tree = buildTree()

    print("=== Calculate Average Per Level By DepthFirst ===")
    result = calculateAveragePerLevel(tree, calculateDepthByDepthFirst)
    print(result)
    assert [4, 8, 6, 6, 2] == result

    print("=== Calculate Average Per Level By BreadthFirst ===")
    result = calculateAveragePerLevel(tree, calculateDepthByBreadthFirst)
    print(result)
    assert [4, 8, 6, 6, 2] == result

    print("=== Transverse Depth First ===")
    result = transverseDepthFirst(tree)
    for elem in result: print(elem.value, end=" : ")
    assert [4,7,10,2,6,2,9,6] == [elem.value for elem in result]

    print("\n=== Transverse Breadth First ===")
    result = transverseBreadthFirst(tree)
    for elem in result: print(elem.value, end=" : ")
    assert [4,7,9,10,2,6,6,2] == [elem.value for elem in result]

if __name__ == '__main__':
    main()