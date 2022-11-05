import os
import CRUD

if __name__ == "__main__":
    operating_system = os.name

    while True:
        match operating_system:
            case "posix":
                os.system("clear")
            case "nt":
                os.system("cls")

        print("==========================")
        print("=Selamat Datang Di Program=")
        print("===Database Perpustakaan===")
        print("===========================")

        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data\n")

        user_input = input("Masukan opsi : ")

        print("\n===========================\n")

        match user_input:
            case "1":
                print("Read Data")
            case "2":
                print("Create Data")
            case "3":
                print("Update Data")
            case "4":
                print("Delete Data")

        print("\n===========================\n")

        is_done = input("Apakah Selesai (y/n) ? ")
        if is_done == "y" or is_done == "Y":
            break

    print("Program Berakhir, Terima Kasih")
