# looping dictionary

teman_teman = {
    "yus" : "Yusril Arzaqi",
    "bim": "Bimo Alam",
    "dam": "Adam Saputra",
    "mas": "Dimas Rafif"
}

# Looping (key)
for teman in teman_teman:
    print(teman)

# operator menggabil item / iterable
keys = teman_teman.keys()
print(keys)

for key in keys:
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for value in values:
    print(values)

items = teman_teman.items()
print(items)

for key, value in items:
    print(f'{key}: {value}') 

