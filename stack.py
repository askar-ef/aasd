class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


# s = Stack()
# s.push(5)
# s.push(12)
# s.push(52)


# print(s.items)
# s.pop()
# print(s.peek())
# print(s.items)
