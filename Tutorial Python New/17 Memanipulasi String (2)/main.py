print("Merubah case dari string")
print("-Merubah semua menjadi upper case")
salam="bro!"
print("String awal :",salam)
salam=salam.upper()
print("String menjadi upper case :",salam)
print("-Merubah semua menjadi lower case")
alay="GuE KheChe AbhiEzzZz"
print("String awal :",alay)
alay=alay.lower()
print("String menjadi lower case :",alay)

print("\nPengecekan dengan isX method")
salam="sist"
apakah_lower=salam.islower()
print("apakah ",salam,"lower case :",apakah_lower)
apakah_upper=salam.isupper()
print("apakah ",salam,"upper case :",apakah_lower)

print("\nCek Komponen startswith(),endswith() ")
cek_start="Yusril Arzaqi".startswith("Yusril")
print("Apakah ","Yusril Arzaqi","Kata pertama Yusril")
print("hasil :",cek_start)
cek_end="Yusril Arzaqi".endswith("Arzaqi")
print("Apakah ","Yusril Arzaqi","Kata terakhir Yusril")
print("hasil :",cek_end)

print("\nPenggabungan Komponen join(), split()")
pisah=["Aku","Beli","Minum"]
gabungan=','.join(pisah)
print(gabungan)
gabungan='..'.join(pisah)
print(gabungan)

print("\nAlokasi Karakter rjust(), ljust(), center()")
kanan="kanan".rjust(10)
print("'",kanan,"'")
kiri="kiri".ljust(10)
print("'",kiri,"'")
center="Tengah".center(10)
print("'",center,"'")
Tengah="HELLO WORLD".center(20,"=")

print("\nKebalikannya strip()")
Tengah=Tengah.strip("=")
print(Tengah)

