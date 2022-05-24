import numpy as np

# Membuat Vector
a = np.array([1,2,3,4,5])
b = np.array([1.5, 2.5, 5, 6, 7])

# Membuat Vector Dengan range
c = np.arange(1,20,2)

# Membuat linspace
d = np.linspace(1,10,4)

# array multidimensi / matrix
e = np.array([(1 ,-1, 0),(-2, 4, 6)])

# matrix dengan nilai nol
f = np.zeros((5,5))

# matrix dengan nilai satu
g = np.ones((5,5))

# matrix identitas
h1 = np.identity(5)
h2 = np.eye(5)

# Display
print(f'{h2}')

