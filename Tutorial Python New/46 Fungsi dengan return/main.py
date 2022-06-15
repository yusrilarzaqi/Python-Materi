""" Fungsi dengan Kembalian """

"""
    template fungsi dengan Kembalian

    def nama_fungsi(argumen):
        badan fungsi
        return output
"""


def kuadrat(input_angka):
    """Fungsi kuadrat"""
    return input_angka**2


output = kuadrat(5)

print(output)
print(kuadrat(10))

z = 10 + kuadrat(12)
print(z)


def fungsi_tambah(angka1, angka2):
    """fungsi untuk menjumlahkan angka1 dan angka2"""
    return angka1 + angka2


x = fungsi_tambah(kuadrat(2), kuadrat(3))
print(x)


def operasi_matematika(angka1, angka2):
    """return tambah, kurang, kali, bagi"""
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah, kurang, kali, bagi


(a, b, c, d) = operasi_matematika(10, 20)

print(f"tambah {a}")
print(f"kurang {b}")
print(f"kali {c}")
print(f"bagi {d}")
