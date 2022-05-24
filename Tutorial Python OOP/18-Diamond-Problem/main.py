class A:
    def s(self):
        print('A')

class B(A):
    # def s(self):
    #    print('B')
    pass

class C(B):
    def s(self):
        print('C')

class D(B,C):
    # def s(self):
    #     print('D')
    pass

foo = D()
foo.s()

