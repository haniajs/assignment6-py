class A:
    def show(self):
        print("Show from A")

class B(A):
    def show(self):
        print("Show from B")

class C(A):
    def show(self):
        print("Show from C")

class D(B, C):  
    pass

d = D()
d.show()  
print(D.__mro__)
