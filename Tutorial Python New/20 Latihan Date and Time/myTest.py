import datetime as dt
from os import system
# from datetime import date
system('clear')

print("Masukan Tanggal, bulan, dan tahun lahir anda ")
day = int(input("day :"))
month = int(input("month : "))
year = int(input("year : "))

tanngal_lahir = dt.date(year, month, day)
hari_ini = dt.date.today()
print(f"Hari ini adalah : {hari_ini}")
ulang_hari = (hari_ini - tanngal_lahir).days
ulang_tahun = ulang_hari // 365
ulang_bulan = (ulang_hari % 365) // 30

print(f'Umur anda adalah : {ulang_tahun} tahun {ulang_bulan} bulan')
