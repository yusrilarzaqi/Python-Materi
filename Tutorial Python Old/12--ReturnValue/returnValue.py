# Return artinya menggembalikan nilai
# maksudnya function itu pertama menginputkan nilai dan bisa mengembalikan dari nilai yang tadi diinputkan
# contoh 1
# pertama mendefinisikan function  
def tambah(a,b):
    return a+b

# lalu memanggil function yang kita sudah buat
# cara membaca 
# membuat var a yang diisi dengan function tambah yang berisi 5 dan 5
a=tambah(5,5)
print(a)
print()
def kali(a,b):
    return a*b

# Bisa juga seperti ini 
b=kali(tambah(5,5),tambah(10,10))
print(b)
