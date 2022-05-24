data_0 = [1, 2]
data_1 = [3, 4]

data_list_biasa = [1, 2, 3, 4]

# print(f'data list biasa : {data_list_biasa}')

list_2D = [data_0, data_1, 6, 7]

# print(f'data 2D : {list_2D}')

# Contoh penggunaan

perserta_0 = ['Ucup', 25, 'laki-laki']
perserta_1 = ['Otong', 10, 'laki-laki']
perserta_2 = ['Dedeh', 50, 'Wanita']

list_peserta = [perserta_0, perserta_1, perserta_2]

print(f'peserta : {list_peserta}')

for peserta in list_peserta:
    print(f'nama\t : {peserta[0]}')
    print(f'umur\t : {peserta[1]}')
    print(f'gender\t : {peserta[2]}\n')

# dengan refrence

list_copy = list_peserta.copy()
print(f'peserta : {list_copy}')
perserta_0[0] = "Michael"
print(f'peserta : {list_copy}')
print(f'peserta : {list_peserta}')
