from stack import Stack
from queueFinal import Queue
from treeFinal import Tree

s = Stack()
q1 = Queue()
q2 = Queue()
t1 = Tree("root")
t2 = Tree("root")
t3 = Tree("root")

# nambah cabang perusahaan
buah1 = input("masukkan buah 1: ")
buah2 = input("masukkan buah 2: ")


def gabung(perusahaan, nama, jenis, value):
    if jenis == buah1:
        if Tree(perusahaan) in t1.children:
            t1.add_value(nama, value)
            print("ada")
        else:
            x = Tree(perusahaan)
            y = Tree(nama, value)
            x.add_child(y)
            t1.add_child(x)
    elif jenis == buah2:
        if Tree(perusahaan) in t2.children:
            t2.add_value(nama, value)
            print("ada")
        else:
            x = Tree(perusahaan)
            y = Tree(nama, value)
            x.add_child(y)
            t2.add_child(x)
    elif jenis == "kardus":
        if Tree(perusahaan) in t3.children:
            t3.add_value(nama, value)
            print("ada")
        else:
            x = Tree(perusahaan)
            y = Tree(nama, value)
            x.add_child(y)
            t3.add_child(x)


# apabila ada barang masuk


def barang_masuk(perusahaan, nama, jenis, value):
    gabung(perusahaan, nama, jenis, value)
    if jenis == buah1:
        q1.enqueue(value)
    elif jenis == buah2:
        q2.enqueue(value)
    elif jenis == "kardus":
        s.enqueue(value)
    else:
        print("Jenis barang yang Anda masukkan salah")

# apabila ada barang keluar


def barang_keluar(jenis, barang):
    if jenis == buah1:
        q1.dequeue(barang)
        s.pop(barang/3)
    elif jenis == buah2:
        q2.dequeue(barang)
        s.pop(barang/2)
    else:
        print("Jenis barang yang Anda masukkan salah")


# apabila ada yang kirim barang

def tambah_barang(nama, jenis, value):
    if jenis == buah1:
        t1.add_value(nama, value)
    elif jenis == buah2:
        t2.add_value(nama, value)


apple = Tree('apple')
harald = Tree('harald', value=3)
cleo = Tree('cleo')
apple.add_child(harald)
apple.add_child(cleo)
t1.add_child(apple)


t1.add_value("cleo", 10)
t1.add_value("cleo", 5)
t1.add_value("cleo", 10)

xiaomi = Tree('xiaomi')
eko = Tree('eko', value=23)
amar = Tree('amar')
xiaomi.add_child(eko)
xiaomi.add_child(cleo)
t2.add_child(xiaomi)


t2.add_value("amar", 20)
t2.add_value("amar", 12)
t2.add_value("amar", 45)

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
        w, x, y, z = input("Masukkan: perusahaan, nama, value: ").split(" ")
        gabung(w, x, y, int(z))
    elif n == 2:
        w, x, y, z = input(
            "Masukkan: perusahaan, nama, jenis, value: ").split(" ")
        barang_masuk(w, x, y, int(z))
    elif n == 3:
        x, y = input("Masukkan: jenis, value").split(" ")
        barang_keluar(x, int(y))
    elif n == 4:
        print("riwayat supplier: ")
        t1.calculate_value()
        t2.calculate_value()
        t3.calculate_value()
        t1.print_tree()
        t2.print_tree()
        t3.print_tree()

    elif n == 5:
        print("gudang buah 1: ", q1.items, "total: ", q1.total())
        print("gudang buah 2: ", q2.items, "total: ", q2.total())
        print("gudang kardus: ", s.items, "total: ", s.total())
    elif n == 6:
        print("total penjualan:")
        print(q1.penjualan)
        print(q2.penjualan)
        x = int(input("harga buah 1: "))
        y = int(input("harga buah 2: "))
        print("total: ", q1.penjualan * x + q2.penjualan * y)
    elif n == 7:
        print("rekap pembelian: ")
        t1.calculate_value()
        t2.calculate_value()
        print(t1.print_firstchild())
        print(t2.print_firstchild())

    elif n.lower() == 'q':
        break

t1.calculate_value()
t2.calculate_value()

t1.print_tree()
t2.print_tree()
