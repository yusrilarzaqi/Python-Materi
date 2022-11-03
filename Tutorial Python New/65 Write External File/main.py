# 1. mode write (creating new file and overriding existing file)

with open("data_1.txt", "w", encoding="utf-8") as file:
    file.write("Yusril Arzaqi")

with open("data_1.txt", "w", encoding="utf-8") as file:
    file.write("Adam Saputra")

# 2. mode append (appending strings to file)

with open("data_2.txt", "w", encoding="utf-8") as file:
    file.write("Adam Saputra\n")

with open("data_2.txt", "a", encoding="utf-8") as file:
    file.write("Yusril Arzaqi\n")

with open("data_2.txt", "a", encoding="utf-8") as file:
    file.write("Bimo Alamsah")

# 3. mode r+ akan menimpa

with open("data_3.txt", "w", encoding="utf-8") as file:
    file.write("ini adalah data ke 3\n")

with open("data_3.txt", "r+", encoding="utf-8") as file:
    file.write("baris 1\n")
    file.write("baris 2\n")

with open("data_3.txt", "r+", encoding="utf-8") as file:
    print(file.read())
