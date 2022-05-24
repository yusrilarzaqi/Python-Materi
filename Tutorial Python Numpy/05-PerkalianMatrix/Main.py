import numpy as np

a = np.array(([1,2], [-2,0]))
b = np.array(([2,2], [-1,3]))

c1 = np.dot(a, b)
c2 = a.dot(b)
c3 = b.dot(a)

print(f"c1 : a.b \n{c1}\nc2 : a.b \n{c2}\nc3 : b.a \n{c3}\n")
