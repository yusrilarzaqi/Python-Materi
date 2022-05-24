import numpy as np

print("1.Membuat Matrix dengan tipe data tertentu")
a = np.array(([1, 2, 3], [4, 5, 6]), dtype=float)
print(a)

print("\n2.Membuat array menggunakan function")
def kuadrat(x):
  return x**2

def jumlah(x, y):
  return x+y
print()
print("np.fromfunction(namafungsi, ukuranMatrix, tipe)") 
b = np.fromfunction(kuadrat, (2, 3), dtype=int)
print(b)
c = np.fromfunction(jumlah, (4, 3), dtype=float)
print()
print(c)

print("\n3.Membuat array dengan iterable")
iterable=(x for x in range(5))
d = np.fromiter(iterable, dtype=int)
print(d)

print("")
