import numpy as np

print("membuat random array")
a = np.floor(np.random.randn(2,2)*10)
print(a)

print(f"nilai max dari a:{a.max()}")
print(f"posisi max dari a:{a.argmax()}")
print(f"nilai min dari a:{a.min()}")
print(f"posisi min dari a:{a.argmin()}")

print("\nSorting")
print(np.sort(a))
print(np.argsort(a))
