class A:
    def s(self):
        print('A')

class B:
    # def s(self):
    #     print('B')

class C(A, B):
    def s(self):
        print('C')

foo = C()
foo.s()
