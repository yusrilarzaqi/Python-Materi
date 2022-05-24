def siswa(nama,kelas,jurusan):
    print('Nama  :',nama)
    print('Kelas :',kelas)
    print('Jurusan :',jurusan)

# statement harus urut
siswa('Yusril',12,'Tkj')
print('\n')
# kalau tidak harus dengan argumennya
siswa(nama='Dimas',kelas=12,jurusan='TKJ')

print('')
# argument default
def penjaga(nama,shift='siang',sifat='baik'):
    print('penjaga sekolan ini bernama :',nama)
    print('shifnya :',shift)
    print('Sifatnya :',sifat)

# jika diberikan argument default akan tidak apapa jika statementnya tidak ditulis tetapi akan ikut defaultnya

penjaga('Heri')
print()
penjaga('Faris','malam','galak')
