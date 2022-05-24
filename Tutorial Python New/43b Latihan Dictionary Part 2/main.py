from datetime import datetime
from os import system
import string, random

# template dict mahasiswa
mahasiswa_template = {
    'nama': 'nama',
    'nim' : '00000000',
    'sks_lulus' : 0,
    'lahir': datetime(2000, 1, 1)
}

data_mahasiswa = {}

while True:
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

    KEY = ''.join((random.choice(string.ascii_uppercase) for _ in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print()
    print('-'*55)
    print(f"{'KEY':<6} {'NAMA':<17} {'NIM':<6} {'SKS LULUS':<5} {'LAHIR':<10} ")
    print('-'*55)
    for mhs in data_mahasiswa:
        KEY = mhs
        NAMA = data_mahasiswa[KEY]["nama"]
        NIM = data_mahasiswa[KEY]["nim"]
        SKS = data_mahasiswa[KEY]["sks_lulus"]
        LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {NIM:<6} {SKS:<5} {LAHIR:^10} ")

    print('\n')
    is_done = input("[y/n]")
    if is_done == 'n' or is_done == 'N':
        break

print('END')