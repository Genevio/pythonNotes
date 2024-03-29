#Handling dimensional problem
class A:
    def display(self):
        print("Op of Class A")

class B(A):
    pass

class C(A):
    pass

class D(C,B):
   pass

o=D()
o.display()