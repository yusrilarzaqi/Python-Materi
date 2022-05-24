# Attribute yang hanya bisa diakses di dalam class saja
# Mendefinisikan class
class mahasiswa():
   __niai= 0
   
   def __init__(self,nama,nis):
      self.nama=nama
      self.nis=nis
   
   def uts(self,input_nilai):
      self.__niai+=input_nilai

   def uas(self,input_nilai):
      self.__niai+=input_nilai
      
   def checkSatus(self):
      if self.__niai<=50:
         print(self.nama,"Tidak Lulus")
      else:
         print(self.nama,"Lulus")

# main program

yusril=mahasiswa("Yusril Arzaqi",185512)
yusril.uts(90)
yusril.uas(70)
yusril.checkSatus()

