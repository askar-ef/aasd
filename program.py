from stack import Stack
from queueFinal import Queue
from treeNew import Tree

s = Stack()
q = Queue()
q2 = Queue()
t = Tree("root")


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


def barang_masuk(perusahaan, nama, barang):
    gabung(perusahaan, nama, barang)
    q.enqueue(barang)


def barang_keluar(jenis, barang):
    if jenis == "jeruk":
        q.dequeue(barang)
    elif jenis == "apel":
        q2.dequeue(barang)
    else:
        print("Jenis barang yang Anda masukkan salah")


def tambah_cabang(jenis, jumlah):
    t.add_child(jenis, jumlah)


def tambah_barang(jenis, jumlah):
    t.add_value(jenis, jumlah)


apple = Tree('apple')
harald = Tree('harald', value=3)
cleo = Tree('cleo')
apple.add_child(harald)
apple.add_child(cleo)
t.add_child(apple)

t.add_value("cleo", 10)
t.add_value("cleo", 5)

t.calculate_value()

t.print_tree()

n = int(input("mau berapa kali: "))
for i in range(n):
    jenis = input("masukin siapa: ")
    jumlah = int(input("masukin berapa: "))
    tambah_barang(jenis, jumlah)

t.calculate_value()
t.print_tree()
