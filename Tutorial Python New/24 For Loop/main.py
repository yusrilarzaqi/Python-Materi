# Perulangan

# angka = 1
# angka2 = [0, 2, 4, 6, 8, 10]

# for i in angka2:
#     print(f'i sekarang -> {i}')

# print("akhir program 1", end="\n\n")
# angka2_range = range(5)

# for i in angka2_range:
#     print(f'i sekarang -> {i}')

# print("akhir program 2", end="\n\n")

# angka2_range = range(1, 5)

# for i in angka2_range:
#     # print(f'i sekarang -> {i}')
#     print(f'hello world ke-{i}')

# print("akhir program 3", end="\n\n")

# Menggunakan string

data_str = "Hello World"
temp = []

for i in range(len(data_str) - 1, -1, -1):
    temp.append(data_str[i])
    # print(i)

print([x for x in temp])
print("akhir program 4", end="\n\n")
