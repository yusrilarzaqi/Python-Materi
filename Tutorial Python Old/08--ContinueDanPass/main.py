print("CONTINUE".center(45,'='))
for i in range(0,10):
   if i==6:
      print("menemukan angka 6")
      continue
   print("Nilai saat ini",i)
else:
   print("menemukan angka 10")
print("di luar loop")