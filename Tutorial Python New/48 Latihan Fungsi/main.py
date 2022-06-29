"""Latihan Fungsi"""
"""program menghitung luas dan keliling persegi panjang"""

# Membuat Fungsi header program
def tampilan(text="Program Menghitung Luas Dan Keliling Persegi Panjang") -> None:
    from os import system

    system("clear")
    print("-" * 150)
    print(f"{text:^150}")
    print("-" * 150)


def input_user() -> tuple:
    """
    Mengambil input user
    """
    lebar = int(input("Masukan Nilai Lebar   : "))
    panjang = int(input("Masukan Nilai Panjang : "))

    return lebar, panjang


def hitung_luas(panjang: int, lebar: int) -> int:
    """fungsi menghitung Luas"""
    return panjang * lebar


def hitung_keliling(panjang: int, lebar: int) -> int:
    """fungsi menghitung keliling"""
    return 2 * (panjang * lebar)


def display(message, value) -> None:
    """fungsi display"""
    print(f"{message} : {value}")


try:
    while True:
        tampilan()
        print(
            """
1. Hitung Luas
2. Hitung Keliling
3. Hitung Semuanya
        """
        )
        option = int(input("> "))
        if option > 3 or option <= 0:
            tampilan("ERROR")
            break

        LEBAR, PANJANG = input_user()

        # Menghitung
        LUAS = hitung_luas(lebar=LEBAR, panjang=PANJANG)
        KELILING = hitung_keliling(lebar=LEBAR, panjang=PANJANG)

        # Tampilkan
        if option == 1:
            display(f"hasil perhitungan Luas     ", LUAS)
        elif option == 2:
            display(f"hasil perhitungan Keliling ", KELILING)
        elif option == 3:
            display(f"hasil perhitungan Luas     ", LUAS)
            display(f"hasil perhitungan Keliling ", KELILING)
        else:
            print("Inputan Anda Salah !! ulangi lagi !! ")
            pass

        isContinue = input("apakah lanjut [y/n] : ")
        if isContinue == "n":
            break
except:
    tampilan("ERROR")
