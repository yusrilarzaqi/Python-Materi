class Ojek():
   def __init__(self,nama,transmisi,daerah):
      self.nama=nama
      self.transmisi=transmisi
      self.daerah=daerah

   def cek_id(self):
      print("Nama :",self.nama,"\nMotor :",self.transmisi,"\nDaerah :",self.daerah)

class Gojek(Ojek):
   
   def cek_id(self):
      print("\nCek di aplikasi\n")


adam=Ojek("Adam","manual","Semarang")
adam.cek_id()
bimo=Gojek("Bimo A","Matic","Ngalian")
bimo.cek_id()



