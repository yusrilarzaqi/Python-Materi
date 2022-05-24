# Latihan perulangan membuat segitiga

sisi = 15

# 1. Menggunakan For

# dummy variable
count = 1

for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir dari for\n")
# Menggunakan while

count = 1
while True:
    print('*'*count)
    count += 1

    if count > sisi:
        break

print("akhir dari for\n")

# 3. hanya ganjil saja

count = 1
spasi = sisi // 2
while True:
    # akan kembali keatas jika ganjil
    if not count % 2 == 1:
        count += 1
        continue

    # akan print jika genap
    print(' '*spasi, "+"*count)
    count += 1
    spasi -= 1

    # akan break jika melebihi sisi
    if count > sisi:
        break


print("akhir dari for\n")
