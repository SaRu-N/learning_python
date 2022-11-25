
class B:
    def __init__(self, b):
        print(b, "Belongs to B")
    def funca(self):
        print("hello b")
class C:
    def __init__(self, c):
        print(c, "Belongs to C")
    def funca(self):
        print("hello c")
        

class A(B,C):
    def __init__(self):
        print("I am derived from A and B")
        super().__init__('A')

a= A()
a.funca()
C.funca(a)

b=A()
print(A.__mro__)
