class A:
    def s(self):
        print("A")


class B(A):
    # def s(self):
    #    print('B')
    pass


class C(A):
    pass
    # def s(self):
    #     print("C")


class D(C):
    def s(self):
        super(D, self).s()

    pass


foo = D()
foo.s()
