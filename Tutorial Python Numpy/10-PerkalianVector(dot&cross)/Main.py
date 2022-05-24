import numpy as np

a = np.array([1, 3])
b = np.array([1, 3])

a2 = np.array([1, 2, 0])
b2 = np.array([2, 1, 0])

print('Perkalian Dot')
c = np.dot(a, b)
c1 = np.dot(a2, b2)
c2 = np.dot(b2, a2)

print(f'{c}\n{c1}\n{c2}')