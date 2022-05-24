print(5*"=","Menyamung Strring (concatenate)")
nama_pertama="Yusril"
nama_tengah="D'"
nama_terakhir="Fance"
nama_lengkap=nama_pertama+" "+nama_tengah+nama_terakhir
print(nama_lengkap)

print("\n",5*"=","Menghitung Panjang String")
Panjang=len(nama_lengkap)
print("Panjang dari nama : ",Panjang)

print("\n",5*"=","Operator Untuk String")
print("Mengecek apakah ada komponen char atau string di string")
d="d"
status=d in nama_lengkap
print("Apakah ",d,"ada di dalam ",nama_lengkap,",hasil :",status)
D="D"
status=D in nama_lengkap
print("Apakah ",D,"ada di dalam ",nama_lengkap,",hasil :",status)
yusril="Yusril"
status=yusril in nama_lengkap
print("Apakah ",yusril,"ada di dalam ",nama_lengkap,",hasil :",status)

print("\nMengulang String")
print("awko"*10)
print(10*"awko")

print("\nIndexing")
print("index ke-0 :",nama_lengkap[0])
print("index ke-(-1) :",nama_lengkap[-1])
print("index ke-[0:3] :",nama_lengkap[0:3])
print("index ke-[2,4,6,8,10] :",nama_lengkap[0:11:2])

print("\nItem Paling Kecil")
print("Paling Kecil : ",min(nama_lengkap))

print("\nItem Paling Besar")
print("Paling Besar : ",max(nama_lengkap))

ascii_code=ord(" ")
print("ASCII code untuk spasi adalah ",ascii_code)

data=117
print("Char untuk ascii 117 adalah ",chr(data))

print("\n",5*"=","Operator dalam bentuk method")
data = "Adam Bimo Dimas Yusril"
jml=data.count("a")
print("Jumblah a dalan ",data,"adalah :",jml)






























