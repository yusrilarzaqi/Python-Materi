from datetime import datetime

mahasiswa1 = {
    'nama': 'Yusril Arzaqi',
    'nim' : '185512',
    'sks_lulus': 100,
    'beasiswa' : True,
    'lahir' : datetime(2003, 7, 23)
}

mahasiswa2 = {
    'nama': 'Dimas Rafif',
    'nim' : '185513',
    'sks_lulus': 150,
    'beasiswa' : True,
    'lahir' : datetime(2003, 4, 3)
}

mahasiswa3 = {
    'nama': 'Adam Saputra',
    'nim' : '185514',
    'sks_lulus': 120,
    'beasiswa' : False,
    'lahir' : datetime(2002, 1, 22)
}

data_mahasiswa = {
    "MHS001": mahasiswa1,
    "MHS002": mahasiswa2,
    "MHS003": mahasiswa3,
}

print('-'*55)
print(f"{'KEY':<6} {'NAMA':<17} {'NIM':<6} {'SKS':<3} {'BEASISWA':<9} {'LAHIR':<10} ")
print('-'*55)

for mhs in data_mahasiswa:
    KEY = mhs
    NAMA = data_mahasiswa[KEY]["nama"]
    NIM = data_mahasiswa[KEY]["nim"]
    SKS = data_mahasiswa[KEY]["sks_lulus"]
    BEASISWA = data_mahasiswa[KEY]["beasiswa"]
    LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")

    print(f"{KEY} {NAMA:<17} {NIM} {SKS} {BEASISWA:^9} {LAHIR} ")