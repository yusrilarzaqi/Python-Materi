data=[1,4,9,16,25,36,49,64]
print("Mengakses List".center(45,"="))
subdata=data[0] # Data index ke-0
print(subdata) 
subdata=data[-3] # Data index ke-(-3)
print(subdata)

print("\n")
print("Memotong List".center(45,"="))
subdata=data[0:4] # menampilkan 0-3 (4 tidak )
print(subdata)
subdata=data[-4:] 
# jika tdk dituliskan maka ambil semua setelahnya
print(subdata)

print("\n")
print("Menambah list".center(45,"="))
data2=[100,200,300,400,500,600,700,800]
data3=data+data2
print(data3)

print("\n")
print("Merubah Content Dari list".center(45,"="))
print("Sebelum\n",data)
data[4]=87
# index ke-4 akan berubah mejadi 87
print("Sesudah\n",data)

# a=data
# a[4]=20
# print(data)
# Tidak mengcopy variable a ke data tapi meng asosiakan a

print("\n")
print("Mengcopy list ke variable baru".center(45,"="))
a=data[:]
# artinya mengcopy semua list kedalam variable baru
a[7]=22200
print(a)

print("\n")
print("Method untuk list".center(45,"="))
data.append(40)
print(data)