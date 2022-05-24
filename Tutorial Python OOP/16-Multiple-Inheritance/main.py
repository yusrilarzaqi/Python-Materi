class A:
    def methodA(self):
        print('Method A')

class B:
    def methodB(self):
        print('Method B')

class C(A, B):
    pass

foo = C()
foo.methodA()
foo.methodB()
