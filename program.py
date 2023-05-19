from stack import Stack
from queueFinal import Queue
from treeFinal import Tree

s = Stack()
q = Queue()
q2 = Queue()
t = Tree("root")

# nambah cabang perusahaan


def gabung(perusahaan, nama, value):
    if Tree(perusahaan) in t.children:
        t.add_value(nama, value)
        print("ada")
    else:
        x = Tree(perusahaan)
        y = Tree(nama, value)
        x.add_child(y)
        t.add_child(x)

# apabila ada barang masuk


def barang_masuk(perusahaan, nama, barang):
    gabung(perusahaan, nama, barang)
    if barang == "jeruk":
        q.enqueue(barang)
    elif barang == "apel":
        q2.enqueue(barang)
    else:
        print("Jenis barang yang Anda masukkan salah")

# apabila ada barang keluar


def barang_keluar(jenis, barang):
    if jenis == "jeruk":
        q.dequeue(barang)
        s.pop(barang/3)
    elif jenis == "apel":
        q2.dequeue(barang)
        s.pop(barang/2)
    else:
        print("Jenis barang yang Anda masukkan salah")


# apabila ada yang kirim barang

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
t.add_value("cleo", 10)

# n = int(input("mau berapa kali nambah barang: "))
# for i in range(n):
#     jenis = input("masukin siapa: ")
#     jumlah = int(input("masukin berapa: "))
#     tambah_barang(jenis, jumlah)

# n = int(input("mau berapa kali nambah cabang: "))
# for i in range(n):
#     perusahaan = input("nama perusahaan: ")
#     nama = input("masukin siapa: ")
#     jumlah = int(input("masukin berapa: "))
#     gabung(perusahaan, nama, jumlah)

# else:
#     apple = Tree('apple')  # sama aja
#     harald = Tree('harald', value=10)
#     apple.add_child(harald)
#     t.add_child(apple)


# n = int(input("mau berapa kali nambah barang: "))
# for i in range(n):
#     jenis = input("masukin siapa: ")
#     jumlah = int(input("masukin berapa: "))
#     tambah_barang(jenis, jumlah)


while True:
    n = int(input("Masukkan pilihan (atau tekan 'q' untuk keluar): "))
    if n == 1:
        x, y, z = input("Masukkan: perusahaan, nama, value: ").split(" ")
        gabung(x, y, int(z))
    elif n == 2:
        x, y, z = input("Masukkan: perusahaan, nama, value: ").split(" ")
        barang_masuk(x, y, z)
    elif n == 3:
        x, y = input("Masukkan: jenis, value").split(" ")
        barang_keluar(x, y)
    elif n == 4:
        t.calculate_value()
        t.print_tree()
    elif n.lower() == 'q':
        break

t.calculate_value()

t.print_tree()
