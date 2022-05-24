# Copy & Pop

teman_teman = {
    "yus" : "Yusril Arzaqi",
    "bim": "Bimo Alam",
    "dam": "Adam Saputra",
    "mas": "Dimas Rafif"
}

# copy dictionary
friends = teman_teman.copy()

print(f'teman teman : {teman_teman}\n')
print(f'friends : {friends}\n')

teman_teman["yus"] = "Arzaqi Yusril"

print(f'teman teman : {teman_teman}\n')
print(f'friends : {friends}\n')

# pop
data_yusril = friends.pop('yus')
print(f'data yusril : {data_yusril}\n')
print(f'friends : {friends}\n')

# popitem
dataTerakhir = friends.popitem()
print(f'data terakhir : {dataTerakhir}\n')
print(f'friends : {friends}\n')

