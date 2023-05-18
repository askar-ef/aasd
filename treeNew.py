class Tree(object):
    "Generic tree node."

    def __init__(self, name='root', value=0):
        self.name = name
        self.children = []
        self.value = value

    def __repr__(self):
        return self.name

    def add_parent(self, parent_node):
        assert isinstance(parent_node, Tree)
        parent_node.add_child(self)

    def add_child(self, child_node):
        assert isinstance(child_node, Tree)
        self.children.append(child_node)

    def calculate_value(self):
        if len(self.children) > 0:
            self.value = sum(child.calculate_value()
                             for child in self.children)
        return self.value

    def print_tree(self, level=0):
        indent = "   " * level
        print(f"{indent}{self.name} {self.value}")
        for child in self.children:
            child.print_tree(level + 1)

    def add_value(self, node, value):
        if self.name == node:
            self.value += value
        else:
            for child in self.children:
                child.add_value(node, value)


# Contoh penggunaan
t = Tree('*')
samsung = Tree('samsung')
enzo = Tree('enzo', 20)
bastian = Tree('bastian', 14)
samsung.add_child(enzo)
samsung.add_child(bastian)
t.add_child(samsung)


def gabung(perusahaan, nama, value):
    x = Tree(perusahaan)
    y = Tree(nama, value)
    x.add_child(y)
    t.add_child(x)


def inputan():
    perusahaan = input("perusahaan: ")
    nama = input("nama: ")
    value = int(input("value: "))
    gabung(perusahaan, nama, value)


# n = int(input("mau berapa kali: "))

# for i in range(n):
#     inputan()

apple = Tree('apple')
harald = Tree('harald', value=3)
cleo = Tree('cleo')
apple.add_child(harald)
apple.add_child(cleo)
t.add_child(apple)

t.add_value("enzo", 30)
t.add_value("cleo", 10)
t.add_value("cleo", 5)

t.calculate_value()

t.print_tree()
