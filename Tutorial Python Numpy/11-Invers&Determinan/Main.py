import numpy as np

a = np.array(([1,-1], [1, 1]))
print(a)

print('\nInvers Matrix')
a_inv = np.linalg.inv(a)
print(a_inv)
print(np.dot(a, a_inv))

print("\nDeterminan Matrix")
det_a = np.linalg.det(a)
print(det_a)
det_a_inv = np.linalg.det(a_inv)
print(det_a_inv)
