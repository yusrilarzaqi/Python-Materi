from datetime import datetime
from os import system

# template dict mahasiswa
mahasiswa_template = {
    'nama': 'nama',
    'nim' : '00000000',
    'sks_lulus' : 0,
    'lahir': datetime(2000, 1, 1)
}

data_mahasiswa = {}

system('clear')

print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print('-'*20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
mahasiswa['nama'] = input("Nama Mahasiswa : ")
mahasiswa['nim'] = input("NIM Mahasiswa : ")
mahasiswa['sks_lulus'] = int(input("SKS Lulus : "))

TAHUN_LAHIR  = int(input("Tahun lahir (YYYY) : "))
BULAN_LAHIR  = int(input("Bulan lahir (1-12) : "))
TANGGAL_LAHIR = int(input("Tanggal lahir (1-31) : "))

mahasiswa['lahir'] = datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

print(mahasiswa)

