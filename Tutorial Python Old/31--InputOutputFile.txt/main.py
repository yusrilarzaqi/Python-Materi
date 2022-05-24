# MEMBUKA FILE.
"""
      w write
      r read only
      a appending
      r+ read dan write
"""

# membuat file
file=open("data.txt","w")

file.write("Membuat file dengan menggunakan python")
file.write("\nIni baris kedua")
file.write("\nIni baris ketiga")
file.write("\nIni baris keempat")

# jangan lupa tutup file
file.close()

# Read a text

file2=open("data.txt",'r')
#print(file2.read())
#print(file2.read(31))
print(file2.readline())

file2.close()

# Menambah isi file

file3=open("data.txt",'a')
file3.write("Ini baris baru menggunakan appending")

file3.close()
