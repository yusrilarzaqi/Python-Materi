import numpy as np

a = np.array(([2, 3], [1, 2]))
y = np.array(([24, 14]))

print(a)
print()
print(y)

a_inv = np.linalg.inv(a)
x1 = a_inv * y
x2 = np.linalg.solve(a, y)

print('a invers',a_inv)
print()
print('x1',x1)
print()
print('x2',x2)