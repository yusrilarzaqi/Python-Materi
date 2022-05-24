print('continue'.center(45,'='))
for i in range(1,10):
    if i==6:
        print('nilai i adalah ',6)
        continue
        # continue berfungsi adalah akan langsung ke awal dan akan mengabaikan baris yang ada di bawahnya
        # print('test')
    print('nilai saat ini',i)
else:
    print('ini di akhir loop')
print('ini di luar loop')

print('PAS'.center(45,'='))
num=6
for i in range(1,10):
    if i is num:
        print('test')
        pass
        # pass == lewati 
    print(i)