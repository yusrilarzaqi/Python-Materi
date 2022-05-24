print('Stack'.center(45,'-'))
tumpukan=[1,2,3,4,5,6]
print(tumpukan)

tumpukan.append(7)
print('memasukan data baru:',7)
print('data sekarang :',tumpukan)
tumpukan.append(8)
print('memasukan data baru:',8)
print('data sekarang :',tumpukan)

out=tumpukan.pop()
print('\n.pop() akan menghapus data yang berada di belakang')
print('\ndata keluar:',out)

print('data sekarang :',tumpukan)

