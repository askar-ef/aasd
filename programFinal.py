from stack import Stack
from queueFinal import Queue
from treeFinal import Tree

s = Stack()
q1 = Queue()
q2 = Queue()
t1 = Tree("root")
t2 = Tree("root")
t3 = Tree("root")


# buah1 = input("masukkan buah 1: ")
# harga1 = input(f"harga {buah1}: ")
# buah2 = input("masukkan buah 2: ")
# harga2 = input(f"harga {buah2}: ")
# harga3 = 2500

buah1 = "jeruk"
buah2 = "apel"
harga1 = 8000
harga2 = 12000
harga3 = 2500

# nambah cabang perusahaan


def gabung(perusahaan, nama, jenis, value):
    if jenis == buah1:
        if Tree(perusahaan) in t1.children:
            for i in t1.children:
                if Tree(nama) not in i.children:
                    if i == Tree(perusahaan):
                        i.add_child(Tree(nama))
                        t1.add_value(nama, value)
                    else:
                        t1.add_value(nama, value)
        else:
            x = Tree(perusahaan)
            y = Tree(nama, value)
            x.add_child(y)
            t1.add_child(x)
    elif jenis == buah2:
        if Tree(perusahaan) in t2.children:
            for i in t2.children:
                if Tree(nama) not in i.children:
                    if i == Tree(perusahaan):
                        i.add_child(Tree(nama))
                        t2.add_value(nama, value)
                    else:
                        t2.add_value(nama, value)
        else:
            x = Tree(perusahaan)
            y = Tree(nama, value)
            x.add_child(y)
            t2.add_child(x)
    elif jenis == "kardus":
        if Tree(perusahaan) in t3.children:
            for i in t3.children:
                if Tree(nama) not in i.children:
                    i.add_child(Tree(nama))
                    t3.add_value(nama, value)
                else:
                    t3.add_value(nama, value)
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
        s.push(value)
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


barang_masuk("FreshMa", "King", "jeruk", 165)
barang_masuk("FreshMa", "Leo", "jeruk", 235)
barang_masuk("FreshMa", "Renal", "jeruk", 305)

barang_masuk("Roir", "Nami", "jeruk", 200)
barang_masuk("Roir", "Hendro", "jeruk", 200)
barang_masuk("Roir", "Jack", "jeruk", 200)

barang_masuk("FreshMa", "Sior", "apel", 100)
barang_masuk("FreshMa", "Lui", "apel", 80)

barang_masuk("Kyuna", "Hanif", "apel", 50)
barang_masuk("Kyuna", "Suga", "apel", 70)
barang_masuk("Kyuna", "Sandra", "apel", 120)

barang_masuk("Optima", "Helga", "kardus", 20)
barang_masuk("Optima", "Sandi", "kardus", 30)

barang_keluar("jeruk", 120)
barang_keluar("jeruk", 45)
barang_keluar("apel", 75)
barang_keluar("apel", 105)


while True:
    n = int(input("Masukkan pilihan (atau tekan 'q' untuk keluar): "))
    if n == 1:
        print(
            """Menu""")  # yang ini jadi ganti buat nampilin perintah2 yang bisa digunain aja
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
        print("persediaan barang di gudang: ")
        print(f"gudang {buah1}: ", q1.items,
              f"\ntotal {buah1} : ", q1.total(), "\n")
        print(f"gudang {buah2}: ", q2.items,
              f"\ntotal {buah2} : ", q2.total(), "\n")
        print("gudang kardus : ", s.items, f"\ntotal kardus: ", s.total(), "\n")
    elif n == 6:
        print("total penjualan:")
        print(f"{buah1} terjual: {q1.penjualan} buah || harga {harga1}")
        print(f"{buah2} terjual: {q2.penjualan} buah || harga {harga2}")
        print("total: ", q1.penjualan * harga1 + q2.penjualan * harga2)
    elif n == 7:
        print("rekap pembelian: ")
        t1.calculate_value()
        t2.calculate_value()
        t3.calculate_value()
        print(t1.print_firstchild())
        print(t2.print_firstchild())
        print(t3.print_firstchild())
    elif n == 8:
        print("Laporan pendapatan bersih: ")
    elif n.lower() == 'q':
        break
