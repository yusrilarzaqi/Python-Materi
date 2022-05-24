# Tehnik Menduplikat List

a = ["Ucup", 'Otong', 'Dudung']
print(f'a = {a}')


b = a  # pass by refrence
print(f'b = {b}')

# Merubah member dari a
print("="*40)

a[1] = "Michael"


print(f'a = {a}')
print(f'b = {b}')

# address dari kedua list a dan b
print("="*40)

print(f'address a : {hex(id(a))}')
print(f'address b : {hex(id(b))}')

# menduplikat list dengan menggunakan copy
print("="*40)
print('Membuat list c dengan a.copy()')

c = a.copy()  # Full duplicate

print(f'address a : {hex(id(a))}')
print(f'address b : {hex(id(b))}')
print(f'address c : {hex(id(c))}')

print("="*40)
print(f'a = {a}')
print(f'b = {b}')
print(f'b = {c}')

print('ubah data c 0')
c[0] = "Dadang"

print(f'a = {a}')
print(f'b = {b}')
print(f'b = {c}')

print('ubah data a 1')
a[0] = "Otong"

print(f'a = {a}')
print(f'b = {b}')
print(f'b = {c}')
