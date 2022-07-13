import sains.matematika
from sains import fisika
from sains.fisika import gaya as g

HASIL = sains.matematika.tambah(10, 20, 30, 40)

print(f"Hasil Tambah : {HASIL}")

HASIL_GAYA = fisika.gaya(90, 10)
print(f"Gaya Aalah : {HASIL_GAYA}")

HASIL_GAYA_1 = g(90, 5)
print(f"Gaya Aalah : {HASIL_GAYA_1}")
