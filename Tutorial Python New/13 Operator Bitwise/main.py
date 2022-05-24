# bitwise adalah operasi masing masing bit

a=9
b=5

print("=======OR========")
c=a|b
print("nilai a :",a,",binary :",format(a,'08b'))
print("nilai b :",b,",binary :",format(b,'08b'))
print("--------------------------------- |")
print("nilai c :",c,",binary :",format(c,'08b'))

print("\n=======AND========")
c=a&b
print("nilai a :",a,",binary :",format(a,'08b'))
print("nilai b :",b,",binary :",format(b,'08b'))
print("--------------------------------- &")
print("nilai c :",c,",binary :",format(c,'08b'))

print("\n=======XOR========")
c=a^b
print("nilai a :",a,",binary :",format(a,'08b'))
print("nilai b :",b,",binary :",format(b,'08b'))
print("--------------------------------- ^")
print("nilai c :",c,",binary :",format(c,'08b'))

print("\n=======NOT========")
c=~a
print("nilai a :",a,",binary :",format(a,'08b'))
print("--------------------------------- ~")
print("nilai c :",c,",binary :",format(c,'08b'))

print("\n====NOT===FLIP====")
d=0b000001001
e=0b111111111
f=d^e
print("nilai d :",d,",binary :",format(d,'08b'))
print("--------------------------------- ~")
print("Nilai not d :",f,",binary :",format(f,'08b'))

