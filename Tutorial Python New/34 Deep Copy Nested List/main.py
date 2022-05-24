from copy import deepcopy
data0 = [1, 2]
data1 = [3, 4]

data_2D = [data0, data1, 10]
data_2D_copy = data_2D.copy()
# data_2D_copy = [data.copy() for data in data_2D]

print(f'data = {data_2D}')
print(f'data copy = {data_2D_copy}')

# mengambil data dari nested list

data = data_2D[0]
# print(f'data = {data}')

# address semuanya

print(f'address asli = {hex(id(data_2D))}')
print(f'address copy = {hex(id(data_2D_copy))}')

print("\naddress dari member ke-1")
print(f'address asli = {hex(id(data_2D[0]))}')
print(f'address copy = {hex(id(data_2D_copy[0]))}')

print()

data_2D[2] = 9
print(f'data = {data_2D}')
print(f'data copy = {data_2D_copy}')

# menggunakan deepcopy

print()

data_2D = [data0, data1, 10]
data_2D_deepcopy = deepcopy(data_2D)

print(f'address asli = {hex(id(data_2D))}')
print(f'address deep = {hex(id(data_2D_deepcopy))}')

print("\naddress dari member ke-1")
print(f'address asli = {hex(id(data_2D[0]))}')
print(f'address copy = {hex(id(data_2D_deepcopy[0]))}')

print()

data_2D[1][0] = 10
data_2D[2] = 9
print(f'data = {data_2D}')
print(f'data copy = {data_2D_copy}')
print(f'data deep = {data_2D_deepcopy}')
