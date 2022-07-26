import numpy as np


data_array = [10, 20, 30, 40, 50]
data = np.array([10, 20, 30, 40, 50])

print(data * 2)
# print(data_array * 2) # <- akan gagal
print([x * 2 for x in data_array])  # <- akan bisa

matrix = np.array([(1, 2), (3, 4)])
print(f"matrix \n{matrix}")
print(f"matrix kuadrat \n{matrix**2}")

zeros_c = np.zeros((2, 2))
print(f"Zeros : \n{zeros_c}")

ones_d = np.ones((2, 2))
print(f"Zeros : \n{ones_d}")

jumlah = matrix + matrix**2 + ones_d
print(jumlah)
