import sains
from sains.matematika import scientific as sci

HASIL = sains.matematika.tambah(10, 20, 30, 40)
print(f"Hasil Tambah : {HASIL}")

HASIL_GAYA = sains.fisika.gaya(90, 10)
print(f"Gaya Aalah : {HASIL_GAYA}")

HASIL_GAYA_1 = sains.fisika.gaya(90, 5)
print(f"Gaya Aalah : {HASIL_GAYA_1}")

HASIL_KALI = sains.matematika.kali(10, 20, 30, 40)
print(f"Hasil KALI : {HASIL_KALI}")

PANGKAT_3 = sci.pangkat(3)
print(f"Hasil 3 PANGKAT 3 : {PANGKAT_3(3)}")

# from sains import *
#
# HASIL = matematika.basic.tambah(10, 20, 30, 40)
# print(f"Hasil Tambah : {HASIL}")
#
# HASIL_GAYA = fisika.gaya(90, 10)
# print(f"Gaya Aalah : {HASIL_GAYA}")
#
# HASIL_GAYA_1 = fisika.gaya(90, 5)
# print(f"Gaya Aalah : {HASIL_GAYA_1}")
#
# HASIL_KALI = matematika.basic.kali(10, 20, 30, 40)
# print(f"Hasil KALI : {HASIL_KALI}")
