print("Program Pembagian")

while True:
   try :
      penyembut=int(input(">>>"))
      pembilang=int(input(">>>"))
      
      hasil=penyembut/pembilang
      print(penyembut,'/',pembilang,'=',hasil)
   except :
      print("anda memasukan huruf")
      