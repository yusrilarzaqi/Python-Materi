# Tutorial membaca file external

print(3 * "=", "Membaca file txt", 3 * "=")

file = open("data.txt", "r")

print(f"status read : {file.readable()}")
# print(f"status write : {file.writable()}")

# baca seluruh file
# print(file.read())

# print(file.readline(), end="") # baca baris pertama
# print(file.readline(), end="") # baca baris kedua
# print(file.readline(), end="") # baca baris ketiga

# baca semua baris sebagai list
print(file.readlines())
print(f"apakah sudah di close ? : {file.closed}")

file.close()
print(f"apakah sudah di close ? : {file.closed}")

# Salah satu membuka file di python menggunakan with
print(3 * "=", "Membaca file txt dengan menggunakan with", 3 * "=")
with open("data.txt", "r") as file:
    content = file.readline()
    print(content, end="")
    print(f"apakah sudah di close ? : {file.closed}")

print(f"apakah sudah di close ? : {file.closed}")
