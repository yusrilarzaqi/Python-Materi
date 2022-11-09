from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk": "XXXXXX",
    "date_add": "yyyy-mm-dd-HH-MM-SS+zzzz",
    "judul": 255*" ",
    "penulis": 255*" ",
    "tahun": "yyyy"
}


def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Database tersedia, init done")
    except:
        print("Database Tidak ditemukan, silahkan membuat database baru")
        Operasi.create_first_database()
