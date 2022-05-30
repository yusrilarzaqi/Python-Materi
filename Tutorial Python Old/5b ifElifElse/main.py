# Operator logika untuk list dan str
gorengan=["bakwan","mendowan","tahu isi","cireng","tahu petis"]
beli="cireng"
## Cara membaca
# jika beli ada di gorengan 
if beli in gorengan:
   # maka 
   print("iya ada ",beli)
# jika beli tidak ada di gorengan
if not beli in gorengan:
   # maka
   print("saya tidak menjual ",beli)

# mencari char 
char="c"
if char in beli:
   print("Ada n")
else:
   print("Tidak ada ",char,"di dalam",beli)
