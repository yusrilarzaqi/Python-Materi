from . import Database
from . import Util
import time


def create_first_database() -> None:

    penulis = input("Penulis : ")
    judul = input("Judul : ")
    tahun_terbit = input("Tahun Terbit : ")

    data = Database.TEMPLATE.copy()

    data["pk"] = Util.random_string(6)
    data["date_add"] = time.strftime("%d-%m-%Y-%H-%M-%S%z", time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = tahun_terbit

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}"

    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print("Something wrong")


def read() -> str:
    try:
        with open(Database.DB_NAME, "r") as file:
            return file.readlines()
    except Exception as err:
        print(f"Error membaca database {err}")
        return False


def create(penulis: str, judul: str, tahun_terbit: int) -> str:

    data = Database.TEMPLATE.copy()

    data["pk"] = Util.random_string(6)
    data["date_add"] = time.strftime("%d-%m-%Y-%H-%M-%S%z", time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = tahun_terbit

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    data_tampil = f"{data['penulis']:.40} | {data['judul']:.40} | {data['tahun']:5}\n"

    try:
        with open(Database.DB_NAME, 'a', encoding='utf-8') as file:
            file.write(data_str)
            return data_tampil
    except:
        print("Something wrong")
