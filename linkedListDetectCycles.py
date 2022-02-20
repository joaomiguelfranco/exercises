

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# This has O(n) time & O(n) space
def has_cycle(list):
    visited = set()
    for elem in list:
        if id(elem) in visited: return 1
        visited.add(id(elem))
    return 0


# This has O(n) time & O(1) space
# Floyd's Cycle Detection Algorithm
# AKA: Tortoise and Hare Algorithm
def has_cyle_with_floyds_cycle_detection_algorithm(list):
    slow = list.head
    fast = list.head
    while slow is not None and fast is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return 1
    return 0

list = [3, 4, 5, 6, 7]
assert has_cycle(list) == 0

list = [3, 4, 5, 5, 7]
assert has_cycle(list) == 1

# LinkedList without cycles
list = [3, 4, 5, 5, 7, 4, 2 ,3, 8, 9]
llist = SinglyLinkedList()
for elem in list:
    llist.insert_node(elem)
assert has_cyle_with_floyds_cycle_detection_algorithm(llist) == 0

# LinkedList with cycles
node = llist.head.next.next.next.next
llist.tail.next = node
assert has_cyle_with_floyds_cycle_detection_algorithm(llist) == 1

