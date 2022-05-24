# looping dari list

# for loop
# kumpulan_angka = [4, 3, 2, 5, 6, 1]

# for i in kumpulan_angka:
#     print(f'{i}')

# peserta = ["ucup", "otong", "dadang", "diding"]

# for nama in peserta:
#     print(f"Nama : {nama}")

# kumpulan_angka = [10, 4, 2, 5, 8, 11]
# panjang = len(kumpulan_angka)

# for i in range(panjang):
#     print(f"{kumpulan_angka[i]}")

# kumpulan_angka = [10, 4, 2, 5, 8, 11]
# panjang = len(kumpulan_angka)
# index = 0

# while index < panjang:
#     print(f"Angka : {kumpulan_angka[index]}")
#     index += 1

# List Comperhension
# data = [
#     "Yusril",
#     2,
#     3,
#     "Bimo" ]

# [print(f'Data : {i}') for i in data]

data_list = [
    "Yusril",
    2,
    3,
    "Bimo"
]

# Enumerate
for i, data in enumerate(data_list):
    print(f"Data {i+1} : {data}")
