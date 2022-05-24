barang=['kunci','ember','jaket','ban','mobil']
print(barang)

print('\nBeberapa method yang bisa digunakan untuk memanipulasi list\n')


print('1.append')
print('fungsinya menambahkan list dari belakang')
barang.append('sepeda')
print(barang)


print('\n2.extend')
print('mambuat itereble sebuah string dam menambahkan di belakangnya')
barang.extend('dompet')
print(barang)

print('\n3.insert')
print('menambahkan list ditengah')
barang.insert(3,'sepeda')
# parameter pertama ialah untuk menambahkan list dari index ke-n
# parameter kedua ialah list yang ingin dimasukan
print(barang)

print('\n4.count')
print('Method untuk menghitung anggota')
jumblahSepeda=barang.count('sepeda')
print('menghitung jumblah sepeda')
print(jumblahSepeda)
print(barang)

print('\n5.remove')
print('menghapus list')
print(barang)
barang.remove('sepeda')
print('menghapus anggota sepeda')
print(barang)
print('remove akan menghapus anggota yang pertama ditemukan')

print('\n6.reverse')
print('membalikan semua isi list')
print('sebelum')
print(barang)
barang.reverse()
print('sesudah')
print(barang)

print('\n7.copy')
print('mengcopy data list kedalam variabel baru')
print('agar tidak sama')
stuff=barang.copy()
stuff.append('gelas')
print('stuff :')
print(stuff)
print('barang :')
print(barang)

