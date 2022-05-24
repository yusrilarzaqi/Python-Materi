# List

# List adah Kumpulan data

# Number

data_angka = [1, 2, 3, ]
print(data_angka)

# Kumpulan data string
data_string = ['Yusril', 'Arzaqi', 'Bimo']
print(data_string)

# Kumpulan data Boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan campuran
data_campuran = [1, "Yusril", True]
print(data_campuran)

# Cara alternatif membuat list
data_range = range(0, 10, 2)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat list dengan for loop, list comprehension
list_using_for = [2**i for i in range(0, 10, 2)]
print(list_using_for)

# Membuat list pake for if
list_using_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_using_for_if)
