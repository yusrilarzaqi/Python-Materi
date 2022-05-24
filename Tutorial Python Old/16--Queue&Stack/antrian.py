from collections import deque

antrian=deque([1,2,3,4,5,6])
print('data awal :',antrian,'\n')

# menambahkan data
antrian.append(7)
print('data masuk:',7)
print('data sekarang :',antrian)

antrian.append(8)
print('data masuk:',8)
print('data sekarang :',antrian)

# mengurangi antrian
# menghapus kiri
out=antrian.popleft()
print('data keluar:',out)
print('data sekarang :',antrian)

out=antrian.popleft()
print('data keluar:',out)
print('data sekarang :',antrian)

out=antrian.popleft()
print('data keluar:',out)
print('data sekarang :',antrian)

antrian.append(9)
print('data masuk:',9)
print('data sekarang :',antrian)
