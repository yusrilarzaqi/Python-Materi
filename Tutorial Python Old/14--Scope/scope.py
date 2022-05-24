# print('scope variable :local'.center(45,'='))

namaKucing='bundel'
makananKucing='royal cannin'

# def rubahNamaKucing(namabaru):
#     namaKucing = namabaru
#     print('saya rubah nama kucing menjadi',namaKucing)

# rubahNamaKucing('kitty')
# print('nama kucing saya mendaji',namaKucing)

print('')

print('scope variable :global'.center(45,'='),'\n')

def rubahNamaKucing1(namabaru):
    global namaKucing
    namaKucing = namabaru
    print('saya rubah nama kucing menjadi',namaKucing)

def kasihMakanKucing(makanan,nama):
    global namaKucing,makananKucing
    namaKucing=nama
    makananKucing=makanan

# rubahNamaKucing1('kitty')
kasihMakanKucing('universal','alex')

print('nama kucing saya menjadi',namaKucing,'dan makan',makananKucing)

# scope local di dalam function
# scope global di luar function
