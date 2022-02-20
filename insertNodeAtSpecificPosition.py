class SinglyLinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def addNext(self, node):
        self.next = node


def buildLinkedList(input):
    head = None
    tail = None
    for elem in input:
        if head == None:
            head = SinglyLinkedListNode(elem)
            tail = head
        else:
            tail.addNext(SinglyLinkedListNode(elem))
            tail = tail.next
    return head

def printLinkedList(llist):
    curNode = llist
    res = []
    while curNode:
        res.append(curNode.data)
        curNode = curNode.next
    return res


def insertNodeAt(llist, data, position):
    curNode = llist
    for index in range(position-1):
        curNode = curNode.next

    tempNode = curNode.next
    newNode = SinglyLinkedListNode(data)
    newNode.next = tempNode
    curNode.next = newNode

    return printLinkedList(llist)

input = [16, 13, 7]
position = 2
data = 1
llist = buildLinkedList(input)
assert insertNodeAt(llist, data, position) == [16, 13, 1, 7]

input = [11, 9, 19, 10, 4]
position = 3
data = 20
llist = buildLinkedList(input)
assert insertNodeAt(llist, data, position) == [11, 9, 19, 20, 10, 4]