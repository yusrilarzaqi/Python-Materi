data_list=[1,2,3,4,5]
data_tuple=(1,2,3,4,5)

print(data_list)
print(type(data_list))
print(data_tuple)
print(type(data_tuple))

print('='*45)

print('Tuple tidak bisa ditambah, dihapus, ataupun dirubah nilainya fix')
print('cara untuk melihat method apa saja yang dapat digunakan tuple')
print(dir(data_tuple))

print("1.count menghitung berapa banyak nilai yang sama ")
print("data_tuple.count(6)")
data_tuple.count(6)
print("2.index menampilkan index melalui nilai")
print("data_tuple.index()")
# index ke n dengan value 5
data_tuple.index(5)

print('\n','='*45)
print("Tipe data tuple lebih ringan dari pada list")
import sys
data_list=[1,2,3,4,5,6,7,8,9,"yusril","Adam","bimo",False]
data_tuple=(1,2,3,4,5,6,7,8,9,"yusril","Adam","bimo",False)

besarDariList=sys.getsizeof(data_list)
besarDariTuple=sys.getsizeof(data_tuple)

print("Besar data dari list :",besarDariList)
print("Besar data dari tuple :",besarDariTuple)

print('\n','='*45)
print("Waktu untuk membuat tuple jauh levih cepat daripada list")
import timeit
data_list=timeit.timeit(stmt="[1-99]",number=1000)
data_tuple=timeit.timeit(stmt="(1-99)",number=1000)
print("Waktu untuk memproses list :",data_list)
print("Waktu untuk memproses tuple :",data_tuple)

