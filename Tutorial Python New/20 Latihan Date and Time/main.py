# Date and time (latihan)

import datetime as dt

# hari_ini = dt.date.today()

# print(hari_ini)
# print(f"Hari ini adalah hari = {hari_ini:%A}")

# tanggal = dt.date(2003, 7, 23)
# print(tanggal)
# print(f"Hari ini adalah hari = {tanggal:%A}")

print("Silahkan masukan tanggal, bulan dan tahun lahir anda")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f'Tanggal lahir anda adalah : {tanggal_lahir}')

hari_ini = dt.date.today()
print(f'hari ini tanggal : {hari_ini}')
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30

print(f'Hari nya adalah : {tanggal_lahir:%A}')
print(f'umur anda adalah : {umur_tahun} tahun {umur_bulan} bulan')
