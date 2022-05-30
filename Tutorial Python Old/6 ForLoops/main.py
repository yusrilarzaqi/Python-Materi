gorengan=["bakwan","mendowan","tahu isi","cireng","tahu petis"]
# cara menampilkan list dengan for loop

print("List sebagai iterable".center(45,"="))
## Cara membaca
# untuk g di dalam gorengan lakukan hal berikut
# g adalah variable yg ada di dalam loop
for g in gorengan:
   # lakukan ini
   print(g)
   # dan ini
   print(len(g))
   # loop akan dieksekusi jika di dalam ini
   # len(g) adalah panjang dari g

print("string sebagai iterable".center(45,"="))
string="bakwan"
for i in string:
   print(i)
   # ini akan di tulis satu satu
   
print("nasted loops atau for dalam for (bersarang)".center(45,"="))
buah=["semangka","melon","pir","pisang"]
sayur=["tomat","kentang","wortel","kangkung"]

daftar_belanja=[gorengan,buah,sayur]
# 
for subDaftarBelanja in daftar_belanja:
   print(subDaftarBelanja)
   for komponen in subDaftarBelanja:
      print(komponen)