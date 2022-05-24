import numpy as np

a = np.arange(10)*2
print(a,'\n')
# Mengambil Nilai
print(f'	Indexing')
print(f'elemen ke-1 dari a :{a[0]}')
print(f'elemen ke-7 dari a :{a[6]}')
print(f'elemen terakhir dari a :{a[-1]}\n')

# Slicing
print(f"	Slicing")
print(f'elemen dari 1-6 adalah {a[0:6]}')
print(f'elemen dari 4 sampai akhir adalah {a[4:]}')
print(f'elemen dari awal sampai 5 adalah {a[:5]}\n')

# Iterasi
print('	Iteration')
for i in a:
  print(f"value :{i}")


