import numpy as np

dtipe=[('nama','S255'),('tinggi',int)]
data=[('Ucup',160), ('Adam',170), ('Bomi',165)]
a = np.array(data, dtype=dtipe)
print(a)
print(np.sort(a, order='tinggi'))
print(np.sort(a, order='nama'))