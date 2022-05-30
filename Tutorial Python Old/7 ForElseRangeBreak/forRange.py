for i in range(0,30,2):
    # start, end, increment
    print(i)
print('='.center(100,'='))
num=3
for i in range(0,10):
    print(i)
    if i is num:
        print('ada angka',3)
        break
        # break akan langsung keluar dari loop dan mengabaikan statement dibawahnya
else:
    print('ini adalah di akhir loop')
print('ini baris di luar loop')
