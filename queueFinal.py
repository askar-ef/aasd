class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self, value):
        if self.is_empty():
            return None
        elif self.items[0] < value:
            value -= self.items[0]
            self.items.pop(0)
            return self.dequeue(value)
        elif self.items[0] == value:
            self.items.pop(0)
        else:
            self.items[0] -= value

    def size(self):
        return len(self.items)

    def total(self):
        total = 0
        for i in self.items:
            total += i
        return total


q = Queue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(5)

q.dequeue(45)

print(q.items)
print(len(q.items))

print(q.total())
