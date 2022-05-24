# Membuat class
class mahasiswa():
   nama="nama"
   
   def belajar(self,kondosi):
      print(self.nama,"sedang belajar",kondosi)
   
   def tidur(self,kondosi):
      print(self.nama,"tidur di kelas",kondosi)

# Main Program
adam=mahasiswa()
bimo=mahasiswa()

adam.nama="Adam Saputra"
bimo.nama="Bimo Alamsyah"

adam.belajar("Matematika")
bimo.belajar("Fisika")

