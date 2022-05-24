# Width and Multiline

# data

data_nama = "Yusril"
data_umur = 19
data_tinggi = 178.3
data_nomor_sepatu = 46

# String
data_string = f'Nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}\n'
print(5*"=" + "Data String" + 5*"=")
print(data_string)

# String Multiline dengan menggunakan enter, new line \n
data_string = f'Nama = {data_nama} \numur = {data_umur} \ntinggi = {data_tinggi} \nsepatu = {data_nomor_sepatu}\n'
print(5*"=" + "Data String Multiline" + 5*"=")
print(data_string)

# String Multiline dengan menggunkanan kutip 3 
data_string = f'''Nama    : {data_nama}
Umur    : {data_umur}
Tinggi  : {data_tinggi}
Sepatu  : {data_nomor_sepatu}
'''
print(5*"=" + "Data String Multiline" + 5*"=")
print(data_string)

# Mengatur lebar
data_string = f'''Nama    : {data_nama:>7}
Umur    : {data_umur:>7}
Tinggi  : {data_tinggi:>7}
Sepatu  : {data_nomor_sepatu:>7}
'''
print(5*"=" + "Data String Multiline" + 5*"=")
print(data_string)























