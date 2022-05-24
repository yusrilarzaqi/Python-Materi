print('======Convert======Celcius=====')
data_cel = float(input('Masukan angka dalam satuan celcius '))

#Pertama celcius ke reamur
print('\n----REAMUR----')
hasil = (4/5)*data_cel
print('hasil dari ',data_cel,' celsius diconvet menjadi \n',hasil,' reamur ')

print('\n----FAHERHEIT----')
hasil = ((9/5)*data_cel) + 32
print('hasil dari ',data_cel,' celsius diconvet menjadi \n',hasil,' faherheit ')

print('\n----Kelvin----')
hasil = data_cel + 273
print('hasil dari ',data_cel,' celsius diconvet menjadi \n',hasil,' Kelvin ')

print('\n======Convert======Reamur=====\n')
data_rea = float(input('Masukan angka dalam satuan reamur '))

print('\n----Celcius----')
hasil = (5/4)*data_rea
print('hasil dari ',data_rea,' reamur diconvet menjadi \n',hasil,' Celcius ')

print('\n----Faherheit----')
hasil = ((9/4)*data_rea)+32
print('hasil dari ',data_rea,' reamur diconvet menjadi \n',hasil,' faherheit ')

print('\n----Kelvin----')
hasil = data_rea + 273
print('hasil dari ',data_rea,' reamur diconvet menjadi \n',hasil,' kelvin ')

print('\n======Convert======Faherheit=====\n')
data_fah = float(input('Masukan angka dalam satuan faherheit '))

print('\n----Celcius----')
hasil = (5/9)*(data_fah-32)
print('hasil dari ',data_fah,' faherheit diconvet menjadi \n',hasil,' Celcius ')

print('\n----Reamur----')
hasil = (4/9)*(data_fah-32)
print('hasil dari ',data_fah,' faherheit diconvet menjadi \n',hasil,' Reamur ')

print('\n----Kelvin----')
hasil = (5/9)*(data_fah-32)+273
print('hasil dari ',data_fah,' faherheit diconvet menjadi \n',hasil,' Kelvin ')










