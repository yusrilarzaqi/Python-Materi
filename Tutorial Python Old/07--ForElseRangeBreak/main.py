for i in range(0,10,2):
   # frist ,end ,increment
   print(i)
num=5
print("Break".center(45,"="))
for i in range(0,100,10):
   print(i)
   # break akan berhenti dan mengabaikan statement di bawahnya
   if i is num:
      print("Angka sudah 50 ditemukan")
      break
else:
	print("Angka tidak ditemukan")

print("Ini sudah di luar for")