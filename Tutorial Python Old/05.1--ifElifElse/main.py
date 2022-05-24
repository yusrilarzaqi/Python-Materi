## If dalam bahasa java script
# if(nilai==75){
#     console.log("Nilai anda :"+nilai)
# }

# if di bahasa python
nilai=75
if nilai==75:
   print("nilai anda :",nilai)

print("\n")
# Nasted if
nilai1=70
nilai2=80

if nilai1==70:
   print("nilai 1 anda :",nilai1)
   print("Step 1")
   if nilai2==80:
      print("Nilai 2 anda :",nilai2)
      print("Step 2")
# jika step 1 tidak bekerja maka step 2 tidak akan di eksekusi

# jika tidak sama dengan
nilai=80
if nilai!=90:
   print("Nilai anda tidak 90")

# Elif 
nilai=90
if 80 <= nilai <= 100:
   print("A")
elif 70 <= nilai < 80:
   print("B")
elif 60 <= nilai < 70:
   print("B+")
elif 50 <= nilai < 60:
   print("C")
else:
   print("F")


