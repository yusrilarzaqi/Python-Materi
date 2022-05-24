# break

from os import system
system('clear')


# num = 0

# while True:
#     num += 1
#     print(f'angka sekarang -> {num}')

#     if num is dataInt:
#         print('THREE')
#         break

#     print('in while loop')


dataInt = int(input("hitung sampai : "))

num = 0

while True:
    num += 1
    # print(f'angka sekarang -> {num}')
    print(f'count = {num}')

    if num is dataInt:
        print('THREE')
        break

    print('in while loop')

print('finish')
