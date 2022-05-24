# while argument:
#     statement 
# ini adalah struktur while 

# contoh 1 (infinite loops)
# while True:
#     print('hello')
# ini akan di lakukan terus menerus tiada akhir 

# contoh 2 loop dengan keadaan
# num=0
# while num<10:
#     print(num)
#     num+=1

# while yang di hentikan oleh user
# ulang=True
# while ulang:
#     print('hello')
#     user=input('[y/n]')
#     if user=='y':ulang=True
#     elif user=='n':ulang=False
#     else:print('ERROR')

# contoh 3 
# start=True
# num=0
# while start:
#     print('di dalam loops')
#     if num==100:
#         start==False
#         print('angka 100 sudah ditemukan')
#     print(num)
#     num+=1

# else
# print('ELSE'.center(45,'='))
# num=0
# while num<=5:
#     print('nilai :',num)
#     num+=1
# else:
#     # berfungsi menampilkan ketika while sudah selesai
#     print('ini diakhir loop while')

# # break
# num=0
# print('BREAK'.center(45,'='))
# while num<10:
#     print('nilai :',num)
#     if num==5:
#         print('angka : sudah ditemukan')
#         break
#         # break digunakan untuk mengentikan loop
#     num+=1

# continue
num=0
while num<10:
    print('nilai :',num)
    if num==5:
        continue
    print(num)
    num+=1
