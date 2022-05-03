from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.a = Stack()
        self.b = Stack()

    def enqueue(self, val):
        self.a.push(val)

    def dequeue(self):
        if self.b.is_empty():
            while not self.a.is_empty():
                transfer = self.a.pop()
                self.b.push(transfer)
        return self.b.pop()
