""" Global & Local Variable"""

nama_global = "Yusril Arzaqi"  # <- INI GLOBAL VARIABLE

# akses variable global dalam fungsi
def fungsi() -> None:
    print(f"fungsi Menampilkan {nama_global}")


fungsi()

# akses variable global dalam loop
for i in range(5):
    print(f"loop {i} : {nama_global}")

# akses variable global dalam percabangan
if True:
    print(f"percabangan : {nama_global}")


# VARIABLE LOCAL SCOPE


def fungsi2():
    nama_local = "Arzaqi Yusril"  # j <- VARIABLE LOCAL SCOPE


fungsi2()
# print(nama_local) tidak bisa dilakukan

## Contoh 1: penggunaan akses variable
def say_yusril():
    print(f"Hello {nama}")


nama = "Yusril"
say_yusril()

## Contoh 2: Merubah variable global

angka = 0


def ubah(angka_baru, nama_baru):
    global angka  # fungsi ini mendapat akses merubah global variable
    global nama
    angka = angka_baru
    nama = nama_baru


print(f"Sebelum {angka}")
print(f"Sebelum {nama}")
ubah(10, "Arzaqi")
print(f"Sesudah {angka}")
print(f"Sesudah {nama}")

# contoh 3
num = 0

for i in range(10):
    num += i
    num1 = 0

print(f"num : {num}")
print(f"num1 : {num1}")

if True:
    num = 10
    num1 = 0

print(f"num : {num}")
print(f"num1 : {num1}")
