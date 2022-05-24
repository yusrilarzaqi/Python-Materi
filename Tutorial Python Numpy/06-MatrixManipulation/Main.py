import numpy as np

a = np.array(([1, 2, 3], [4, 5, 6]))
print(f'Matrix a dengan ordo :{a.shape}')
print(a,"\n")

print("TRANSPOSE".center(10,'='))
print(f'Transpose Matrix a :')
print(f'{a.transpose()}')
print(f'{np.transpose(a)}')
print(f'{a.T}\n')

print("FLATTEN Array".center(10,"="))
print("FLATTEN Matrix a :")
print(a.ravel())
print(np.ravel(a),"\n")

print("Reshape".center(10, '='))
print("Reshape Matrix a :")
print(a.reshape(1,6),'\n')

print("Resize".center(10, '='))
a.resize(6,1)
print(a)

