# Program list buku

list_buku = []
while True:
    print(f"Masukan data buku")
    judul = input("Masukan Judul\t: ")
    penulis = input("Masukan Penulis\t: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("\n")
    print("="*10, "DATA BUKU", "="*10)
    for i, buku in enumerate(list_buku):
        print(f"{i+1} | {buku[0]}  | {buku[1]}")

    print("\n\n", "="*20)
    isLanjut = input("continue ? [y/n]}")

    if isLanjut == 'n':
        break

print("prgram end")
