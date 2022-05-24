class Mangga:
    # Magic method (keyword yang sudah ada di python)
    def __init__(self, jumlah):
        # Method pertama kali dieksekusi apabila class terpanggil
        self.__jumlah = jumlah

    def __repr__(self):
        # Merubah output objek menjadi yang kita inginkan, digunqkan sebagai debug
        pass

    def __str__(self):
        # Prilakunya sama dengan __repr__, digunakan jika programya sudah jadi
        pass

    def __add__(self, obj):
        # Melakukan Perhitungan matematik(penjumplahan)
        return self.__jumlah + obj.__jumlah

   #  def __dict__(self):
        #merubah tamplian __dict__
     #    pass

objek = Mangga(5)
objek1 = Mangga(7)
objek.__add__(objek1)
print(objek.__dict__)

