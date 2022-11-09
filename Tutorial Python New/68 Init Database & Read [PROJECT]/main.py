import CRUD as Crud
import os

if __name__ == "__main__":

    os.system('clear')
    print("==========================")
    print("=Selamat Datang Di Program=")
    print("===Database Perpustakaan===")
    print("===========================")

    # check database itu ada atau tidak
    Crud.init_console()

    while True:
        os.system("clear")

        print("==========================")
        print("=Selamat Datang Di Program=")
        print("===Database Perpustakaan===")
        print("===========================")

        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data\n")

        user_input = input("Masukan opsi : ")

        print()
        match user_input:
            case "1": Crud.read_console()
            case "2": print("Create Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")

        print()
        is_done = input("Apakah Selesai (y/n) ? ")
        if is_done == "y" or is_done == "Y":
            break

    print("Program Berakhir, Terima Kasih")
