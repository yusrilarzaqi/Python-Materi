# Operasi

# index   0        1        2
data = ['Ucup', 'Otong', 'Dudung']

# mengambil data dari List
print(f'data pertama (index 0) : {data[0]}')
print(f'data Terakhir          : {data[-1]}')
print(f'data Ucup              : {data[-3]}')

# mengambil info junlah data dalam list
panjang_data = len(data)
print(f'panjang data           : {panjang_data}')

# Memanipulais data

# Menambahkan item pada list sesuai posisi
print(f'data sebelum ditambah : {data}')
data.insert(1, "Asep")
print(f'data sesudah ditambah : {data}')

# Menambahkan di akhia rlist
data.append('jajang')
print(f'data ditambah lagi    : {data}')

# menambahkan lsit dengan list

data_baru = ['Ujang', 'Usep', 'Dadang']
data.extend(data_baru)
print(f'data gabungan         : {data}')

# Ubuah data ke 2 menjadi micheal
data[2] = 'Michael'
print(f'data rubah            : {data}')

# Remove data
data.remove('Ujang')
print(f'data remove           : {data}')
# data.remove('usep') # Akan eror karnea case sensitive

# Meremove data paling belakang
data.pop()
print(f'data remove terakhir  : {data}')
