""" Module matematika dengan import """

from matematika import tambah as t
from matematika import kali as k
from matematika import pangkat as p

import matematika as math

hasil_tambah = t(1, 2, 3, 4, 5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = k(1, 2, 3, 4, 5)
print(f"hasil kali = {hasil_kali}")

pangkat3 = p(3)
print(f"hasil pangkat = {pangkat3(3)}")
