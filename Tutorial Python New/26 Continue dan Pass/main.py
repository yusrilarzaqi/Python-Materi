# continue, pass, break

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi

# num = 0

# while num < 5:
#     num += 1
#     if num == 3:
#         # print("three")
#         pass
#     print(num)

# continue

num = 0

print(f'angka sekarang -> {num}')

while num < 5:
    num += 1
    print(f'angka sekarang -> {num}')

    if num == 3:
        print('three')
        continue

    print("in while")

print('end')
