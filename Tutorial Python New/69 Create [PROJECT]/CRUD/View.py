from .Operasi import read, create


def read_console() -> None:
    data_file = read()

    # variables
    no = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    print("="*100)
    # header
    print(f"{no:4} | {judul:40} | {penulis:40} | {tahun:5} ")
    print('-'*100)

    # data
    for index, data in enumerate(data_file):
        data_break = data.split(',')

        print(
            f"{index+1:4} | {data_break[2]:.40} | {data_break[3]:.40} | {data_break[4]:5}", end="")

    print("="*100)


def create_console() -> None:
    print("="*100, end="\n\n")
    penulis = input("Penulis : ")
    judul = input("Judul : ")

    while True:
        try:
            tahun_terbit = int(input("Tahun Terbit : "))

            if len((str(tahun_terbit))) != 4:
                print("Tahun is Invalid")
                continue

            break
        except:
            print("Tahun must number")

    # print()
    # print("="*100)

    # print(f"{'Judul':40} | {'Penulis':40} | {'Tahun':5} ")
    # print('-'*100)
    # print(create(penulis, judul, tahun_terbit))

    read_console()
