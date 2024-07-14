class A:
     def hi(self):
         print("hello")
class B(A):
    def __init__(self):
        print("hello 2")
class C(A):
    def __init__(self):
        print("hello3")
b=B()
b.hi()
c=C()
c.hi()