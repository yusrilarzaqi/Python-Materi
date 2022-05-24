# definisi class
class mahasiswa():
   nama="nama"
   jurusan=""
   kelas=None
   
   # jika menggunakan __init__ akan dimasukan saat kita membuat object
   def __init__(self,nama,kelas,jurusan):
      self.nama=nama
      self.kelas=kelas
      self.jurusan=jurusan
   
   def belajar(self,kondisi):
      print(self.nama,"sedang belajar",kondisi)
      
   def tidur(self,kondisi):
      print(self.nama,"sedang tidur di kelas",kondisi)

# main program
yusril=mahasiswa("Yusril Arzaqi",12,"TKJ")
print(yusril.nama)
print(yusril.kelas)
print(yusril.jurusan)
yusril.belajar("Administrasi Sistem Jaringan")


