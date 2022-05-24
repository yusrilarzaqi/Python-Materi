# >,<,>=,<=,==,!=,is,is not
a=4
b=2
print("a = 4")
print("b = 2")

print("===========Lebih dari > ")
hasil=a>3
print(a,'>',3,'=',hasil)
hasil=b>3
print(b,'>',3,'=',hasil)
hasil=b>2
print(b,'>',2,'=',hasil)

print("===========Kurang dari < ")
hasil=a<3
print(a,'<',3,'=',hasil)
hasil=b>3
print(b,'<',3,'=',hasil)
hasil=b>2
print(b,'<',2,'=',hasil)

print("===========Lebih dari sama dengan >=")
hasil=a>=3
print(a,'>=',3,'=',hasil)
hasil=b>3
print(b,'>=',3,'=',hasil)
hasil=b>2
print(b,'>=',2,'=',hasil)

print("===========Kurang dari sama dengan <=")
hasil=a>=3
print(a,'<=',3,'=',hasil)
hasil=b>3
print(b,'<=',3,'=',hasil)
hasil=b>2
print(b,'<=',2,'=',hasil)

print("===========Sama dengan ==")
hasil=a==3
print(a,'==',3,'=',hasil)
hasil=b>3
print(b,'==',3,'=',hasil)
hasil=b>2
print(b,'==',2,'=',hasil)

print("===========Tidak sama dengan !=")
hasil=a!=3
print(a,'!=',3,'=',hasil)
hasil=b>3
print(b,'!=',3,'=',hasil)
hasil=b>2
print(b,'!=',2,'=',hasil)

print("===========is (membandingkan obj)")
x=5
y=5
print("nilai x =",x,",id =",hex(id(x)))
print("nilai x =",x,",id =",hex(id(y)))
hasil=x is y
print("x is y =",hasil)

print("===========is not (membandingkan obj)")
x=5
y=5
print("nilai x =",x,",id =",hex(id(x)))
print("nilai x =",x,",id =",hex(id(y)))
hasil=x is not y
print("x is not y =",hasil)
