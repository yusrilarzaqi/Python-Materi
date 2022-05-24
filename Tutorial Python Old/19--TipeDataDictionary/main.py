print("Cara membuat tipe data dictionary".center(45,'='))
print(r"""variable={key:value,
          key:value
}""")
print('')

print("Contoh Dictionary".center(45,'='))
member1={"ID":101,
   "Nama":"Yusril arzaqi",
   "Pekerjaan":"Pelajar",
   "Status member":"Vvip"
}
print(member1)
print('\n')

print('\n')
print("Menampilkan dengan keywordnya".center(45,'='))
print("ID :",member1["ID"])

print('\n')
print("Menampilkan semua keynya".center(45,'='))
print(member1.keys())

print('\n')
print("Menampilkan value nya".center(45,'='))
print(member1.values())

print('\n')
print("Cara lain untuk menampilkan seluruh item".center(45,'='))
print(member1.items())

member2={"ID":102,
"Nama":"Bimo Alamsyah",
"Pekerjaan":"Admin",
"Status member":"member"
}
print('\n')
print('='*45)
list_member={101:member1,102:member2}

print(list_member[101])


