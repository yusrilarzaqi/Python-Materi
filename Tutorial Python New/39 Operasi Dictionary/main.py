# Operator dictionary

data_dict = {
    "yus" : "Yusril Arzaqi",
    "bim": "Bimo Alam",
    "dam": "Adam Saputra",
}

# Panjang dictionary
LENDICT = len(data_dict)
print(f'Panjang dictionary {LENDICT}')

# mengecek key exist atau tidak
KEY = 'yus'
CHECKKEY = KEY in data_dict
print(f'apakah {KEY} ada di data_dict: {CHECKKEY}')

# Mengakses value (key) menggunakan method get
print(data_dict["bim"])
print(data_dict.get('bim'))
print(data_dict.get('get', 'key not found')) # check key with message

# update data
data_dict["yus"] = "Arzaqi Yusril"
print(data_dict)
data_dict['mas'] = "DImas Rafif"
print(data_dict)

data_dict.update({"yus": "Yusril Arzaqi"})
print(data_dict)
data_dict.update({"bukh": "Bukhori Muslim"}) # kalau tidak ada akan menambahkan
print(data_dict)

# Mendelete data dictionary
del data_dict["bukh"]
print(data_dict)

