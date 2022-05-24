## Operasi yang dapat dilakukan dengan penugasan
a=5

# ARITMATIKA
print("=========================ARITMATIKA")
a+=1 
print("a+=1",",Artinya a = a+1 ,hasil :",a)

a-=2 
print("a-=2",",Artinya a = a-2 ,hasil :",a)

a*=2 
print("a*=2",",Artinya a = a-2 ,hasil :",a)

a/=2 
print("a/=2",",Artinya a = a/2 ,hasil :",a)

print("\n===========================BITWISE")

print("======================= (|)")
c=True
c|=False
print("c = True")
print("c |= False","Artinya c = c|False ,hasil :",c)
c=False
c|=False
print("c = False")
print("c |= False","Artinya c = c|False ,hasil :",c)

print("======================= (&)")
c=True
c&=False
print("c = True")
print("c &= False","Artinya c = c&False ,hasil :",c)
c=True
c&=True
print("c = True")
print("c &= True","Artinya c = c&True ,hasil :",c)

print("======================= (^)")
c=True
c^=False
print("c = True")
print("c ^= False","Artinya c = c^False ,hasil :",c)
c=True
c^=True
print("c = False")
print("c ^= False","Artinya c = c^False ,hasil :",c)

print("\n===========================GESER")
print("======================= (>>)")
d=0b01001
print("nilai d =",d,'d >>= 2 , Artinya d = d  >> 2 ')
d>>=2
print("hasil :",d)
print("======================= (<<)")
d=0b01001
print("nilai d =",d,'d <<= 1 , Artinya d = d  << 1 ')
d<<=1
print("hasil :",d)

