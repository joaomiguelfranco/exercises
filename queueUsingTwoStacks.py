class stack:
    def __init__(self):
        self.s = []
    def top(self):
        return self.s[0]
    def push(self, val):
        self.s.append(val)
    def pop(self):
        return self.s.pop(0)
    def isEmpty(self):
        return len(self.s) == 0

class queue:
    def __init__(self):
        self.front = stack()
        self.rear = stack()

    def enqueue(self, val):
        self.rear.push(val)

    def print(self):
        self.__fillFrontStack()
        print(self.front.top())

    def __fillFrontStack(self):
        if self.front.isEmpty():
            while not self.rear.isEmpty():
                self.front.push(self.rear.pop())

    def dequeue(self):
        self.__fillFrontStack()
        if not self.front.isEmpty():
            self.front.pop()



q = queue()
q.enqueue(42)
q.dequeue()
q.enqueue(14)
q.print()
q.enqueue(28)
q.print()
q.enqueue(60)
q.enqueue(78)
q.dequeue()
q.dequeue()
q.print()

print("====")
q = queue()
q.enqueue(42)
q.print()
q.enqueue(14)
q.enqueue(28)
q.enqueue(60)
q.enqueue(78)
q.dequeue()
q.dequeue()
q.print()