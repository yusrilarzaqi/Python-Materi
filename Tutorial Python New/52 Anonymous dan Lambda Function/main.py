""" Anonymous Function & Lambda Function """


def f_kuadrat(x) -> int:
    return x**2


OUTPUT = f_kuadrat(10)
print(f"hasil fungsi kuadrat = {OUTPUT}")

# LAMBDA
# output = lambda argument: expression
kuadrat = lambda angka: angka**2

OUTPUT = kuadrat(10)
print(f"hasil lambda kuadrat = {OUTPUT}")

pangkat = lambda number, pow: number**pow

OUTPUT = pangkat(10, 2)
print(f"hasil lambda pangkat = {OUTPUT}")

## Kegunaan

# sorting list yang biasa
data_list = ["Yusril", "Arzaqi", "Bimo", "Dimas", "Adam"]
data_list.sort()
print(f"Sorted List {data_list}")

# sorting list pakai panjang
def panjang_nama(nama):
    return len(nama)


data_list.sort(key=panjang_nama)
print(f"Sorted List Len {data_list}")

# Sorting pakai lambda

data_list.sort(key=lambda nama: len(nama))
print(f"Sorted List Lambda {data_list}")

# Filter
data_angka = [x for x in range(1, 13)]


def kurang_dari_lima(number) -> int:
    return number < 5


# data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru = list(filter(lambda num: num < 5, data_angka))

print(f"Data Angka Baru = {data_angka_baru}")

# Genap

data_genap = list(filter(lambda num: num % 2 == 0, data_angka))
print(f"Data Genap = {data_genap}")

# ganjil
data_ganjil = list(filter(lambda num: num % 2 == 1, data_angka))
print(f"Data Ganjil = {data_ganjil}")

# Kelipatan 3
data_kelipatan_tiga = list(filter(lambda num: num % 3 == 0, data_angka))
print(f"Data Kelipatan Tiga = {data_kelipatan_tiga}")

# Anonymous Function
# currying <- Haskell Curry

# fungsi biasa
def f_kuadrat(x) -> int:
    return x**2


# Dengan currying
def pangkat(n):
    return lambda angka: angka**n


pangkat2 = pangkat(2)
pangkat3 = pangkat(3)

print(f"5 pangkat 2 = {pangkat2(5)}")
print(f"5 pangkat 3 = {pangkat3(5)}")
print(f"pangkat bebas = {pangkat(4)(5)}")
