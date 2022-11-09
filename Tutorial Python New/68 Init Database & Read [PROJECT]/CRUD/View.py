from .Operasi import read


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
