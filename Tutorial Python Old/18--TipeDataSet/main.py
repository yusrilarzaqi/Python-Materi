# set == himpunan

# membuat set
super_hero={"wiro sableng",
   "si buta dari gua hantu",
   "Saras 008",
   "Gundam",
   "Gatot kaca"
}
print(super_hero)

print('\n')
print("Menambah member".center(45,"="))
super_hero.add("Maklampir")
print(super_hero)

print('\n')
print("membuat set dengan cara lainnya".center(45,'='))
marvel=set()
marvel.add("iron man")
marvel.add("Hulk")
marvel.add("Captain Amerika")
marvel.add("Thor")
print(marvel)

print('\n')
print('Penggabungan'.center(45,'='))
ganjil={1,3,5,7,9}
genap={2,4,6,8}
prima={2,3,5,7}

print(ganjil.union(genap))

print('\n')
print("Irisan".center(45,'='))

print(ganjil.intersection(prima))

