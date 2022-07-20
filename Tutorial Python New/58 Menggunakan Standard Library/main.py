import datetime

data_waktu = datetime.datetime.now()

print(f"Date Time {data_waktu}")
print(f"Jam {data_waktu.strftime('%I:%M:%S')}")
print(f"Hari {data_waktu.strftime('%A')}")
print(f"Bulan {data_waktu.strftime('%m')}")
print(f"Tahun {data_waktu.year}")

from collections import Counter

data = ["a", "b", "c", "d", "a", "d", "e", 'a', 'a']
data_count = Counter(data)

print(data_count)
print(f"Jumblah a : {data_count['a']}")

import io 

file = io.open('file_text.txt', 'r')

print(file.read())
