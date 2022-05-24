# definisi class
class mahasiswa():
   jml_mhs=0
   
   def __init__(self,nama,nis):
      self.nama=nama
      self.nis=nis     
      self.jml_mhs+=1

# main program

yusril=mahasiswa("Yusril A",185512)
adam=mahasiswa("Adam S",185513)
bimo=mahasiswa("Bimo A",185514)

print(mahasiswa.jml_mhs)
print(yusril.__dict__)
print(adam.__dict__)
print(bimo.__dict__)

