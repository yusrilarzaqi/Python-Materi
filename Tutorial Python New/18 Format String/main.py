## conoth generik
#string
nama = 'Yusril'
format_str = f'Hello {nama}!'

#angka
angka = 2005.5
format_str = f'angka : {angka}'

#boolean
boolean = True
format_str = f'boolean : {boolean}'

#bilangan bulat
bil_bulat = 15
format_str = f'bilangan bulat : {bil_bulat:d}'

#bilangan Ribuan/Jutaan
bil = 5000000
format_str = f'bilangan jutaan : {bil:,}'

#desimal
desimal = 328.19282
format_str = f'desimal : {desimal:.2f}'

#menampilkan leanding zero
format_str = f'desimal : {desimal:012.3f}'

#menampilkan tanda - dan +
angka_minus = -10
angka_plus = 10
f_min = f'minus : {angka_minus}'
f_plus = f'plus : {angka_plus:+d}'

#memformat persen
persentase = .045
format_persen = f'persentase : {persentase:.2%}'


#operasi aritmatika
a = 2
b = 3
format_str = f'a+b = {a+b}'


#format angka lain (binary, octal, hexadecimal)
angka = 255

f_bin = f'{bin(angka)}'
f_octal = f'{oct(angka)}'
f_hex = f'{hex(angka)}'




print(f_bin)
print(f_octal)
print(f_hex)
