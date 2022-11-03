# input_number = int(input("Masukan Angka : "))

# if input_number is 0 then runtime error (ZeroDivisionError)
# result = 10 / input_number

# print(result)

# error jika data.txt tidak ada
# file = open("data.txt", "r")

# Exception akan terjadi saat program mengalami error saat runtime
## contoh sederhana untuk menangkap exception

from math import nan

## contoh sederhana
# input_number = int(input("Masukan Angka : "))
# result = nan
#
# try:
#     result = 10 / input_number
# except:
#     result = "Zero Division Error"
#
# print(f"Hasil : {result}")

## contoh di aplikasi
# while True:
#     angka = int(input("masukan angka : "))
#     try:
#         hasil = 10 / angka
#         print(f"hasil : {hasil}")
#         is_done = input("lanjut ?\n")
#         if is_done == "n":
#             break
#     except ValueError as ve:
#         print(f"dilarang input string ({ve})")
#     except Exception as e:
#         print(f"pembagi nol, silahkan masukan input lagi ({e})")

# print("akhir dari program")

while True:
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            print(file.read())
        break
    except Exception as e:
        print(f"file data.txt tidak ditemukan ({e})")
        with open("data.txt", "w", encoding="utf-8") as file:
            file.write("Hello World")
        break
