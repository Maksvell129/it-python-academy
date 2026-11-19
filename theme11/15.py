

class A:
    def fly(self):
        print("Летит A")

    def swim(self):
        print("Плывёт A")


class B:
    def fly(self):
        print("Летит B")

    # def swim(self):
    #     print("Плывёт B")


class C(B, A):

    def fly(self):
        super().fly()
        print("Летит С")

c = C()

c.fly()
c.swim()


print(C.mro())

