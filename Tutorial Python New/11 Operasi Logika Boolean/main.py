# not,or,and,xor

print("============not")
a=True
c=not a
print('not',a,'=',c)

print("============or")
a=False
b=False
c=a or b
print(a,'or',b,'=',c)
a=False
b=True
c=a or b
print(a,'or',b,'=',c)
a=True
b=False
c=a or b
print(a,'or',b,'=',c)
a=True
b=True
c=a or b
print(a,'or',b,'=',c)

print("============and")
a=False
b=False
c=a and b
print(a,'and',b,'=',c)
a=False
b=True
c=a and b
print(a,'and',b,'=',c)
a=True
b=False
c=a and b
print(a,'and',b,'=',c)
a=True
b=True
c=a and b
print(a,'and',b,'=',c)

print("============xor")
a=False
b=False
c=a xor b
print(a,'xor',b,'=',c)
a=False
b=True
c=a xor b
print(a,'xor',b,'=',c)
a=True
b=False
c=a xor b
print(a,'xor',b,'=',c)
a=True
b=True
c=a xor b
print(a,'xor',b,'=',c)

