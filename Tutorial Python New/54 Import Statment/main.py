# import statment

# fungsinya adalah untuk mengambil program dari file lain external.py

# 1. Untuk menyambung program dari external file dan menjalankannya
import program_print
import program_ucup


# 2. import dengan data
import variable
import variable1

# data ada di namespace variable
print(variable.NAME)
print(variable1.NAME)

import matematika

HASIL = matematika.tambah(10, 20)
print(f"Hasil dari import matematika {HASIL}")
