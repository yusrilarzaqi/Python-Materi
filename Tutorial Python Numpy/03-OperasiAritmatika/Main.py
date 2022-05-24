import numpy as np

# list python
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 8, 9, 10]

# array numpy
anp = np.array([1, 2, 3, 4, 5])
bnp = np.array([6, 7, 8, 9, 10])

## ELEMENTWISE
# Penjumlahan
hasil = anp + bnp

# Pengurangan 
hasil = anp - bnp

# perkalian 
hasil = anp * bnp

# Pembagian
#hasil = anp / bnp

#Kuadrat
#hasil = anp**2

# Multidimensi numpy
c = np.array([(1, 0, 1), (2, 0, 2)])
d = np.array([(0, 1, 0), (0, 2, 0)])

#hasil = c + d
#hasil = c - d
#hasil = c * d

print(hasil)
