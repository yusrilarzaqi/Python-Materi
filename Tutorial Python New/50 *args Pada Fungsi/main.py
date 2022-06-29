""" *args """

# Memasukan data/argument


from types import resolve_bases


def fungsi(nama, tinggi, berat):
    print(f"nama:\t{nama}\ntinggi:\t{tinggi}\nberat:\t{berat}")


fungsi("Yusril Arzaqi", 180, 90)

print()


def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"nama:\t{nama}\ntinggi:\t{tinggi}\nberat:\t{berat}")


fungsi(["Yusril Arzaqi", 180, 90])

print()


def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"nama:\t{nama}\ntinggi:\t{tinggi}\nberat:\t{berat}")


fungsi("Yusril Arzaqi", 180, 90)

print()

# Studi kasus


def tambah(*data: int) -> int:
    result = 0
    for i in data:
        result += i

    return result


OUTPUT = tambah(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"HASIL : {OUTPUT}")
