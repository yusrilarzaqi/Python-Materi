data_angka = [1, 5, 1, 4, 3, 2, 4, 3, 2, 3, 7, 8, 9, 0]

print(f'data angka : \n{data_angka}')

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f'jumlah data 4 : {jumlah_data_4}')
print(f'jumlah data 3 : {jumlah_data_3}')

# ambil posisi data index

data = ['Ucup', 'Otong', 'Dudung', 'Ujang']

print(f'data : \n{data}')

index_dudung = data.index('Dudung')
index_ujang = data.index('Ujang')
print(f'Index Dudung : {index_dudung}')
print(f'Index Ujang  : {index_ujang}')

# mengurutkan List
print(f'Data angka sebelum diurutkan : \n{data_angka}')
data_angka.sort()
print(f'Data angka sesudah diurutkan : \n{data_angka}')

print(f'Data sebelum diurutkan : \n{data}')
data.sort()
print(f'Data sesudah diurutkan : \n{data}')

# balik listnya
data_angka.reverse()
data.reverse()
print(f'data direverse : \n{data_angka} \n{data}')
