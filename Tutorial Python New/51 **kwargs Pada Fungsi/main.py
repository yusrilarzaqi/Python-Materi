""" *kwargs """


def fungsi(nama, tinggi, berat):
    """fungsi biasa"""
    print(f"nama:\t{nama}\ntinggi:\t{tinggi}\nberat:\t{berat}")


fungsi("Yusril Arzaqi", 180, 90)

print()


def fungsi(**kwargs):
    """fungsi **kwargs"""
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"nama:\t{nama}\ntinggi:\t{tinggi}\nberat:\t{berat}")


fungsi(nama="Yusril Arzaqi", tinggi=180, berat=90)

print()

# Studi kasus


def math(
    *args,
    **kwargs,
):
    result = 0
    if kwargs["options"] == "tambah":
        for angka in args:
            result += angka
    if kwargs["options"] == "kali":
        result = 1
        for angka in args:
            result *= angka
    else:
        print("Tidak ada operasi")

    return result


OUPUT = math(1, 2, 3, 4, 5, 6, options="tambah")
print(f"hasil jumlah : {OUPUT}")
OUPUT = math(1, 2, 3, 4, 5, 6, options="kali")
print(f"hasil kali   : {OUPUT}")
