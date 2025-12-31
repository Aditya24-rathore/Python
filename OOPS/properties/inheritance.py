# inheritance :- parent - child relation
# MRO- metod resolutio order MRO use DFS algorithm(Depth first search)
# Types of inheritance
# method overridding
# Single level inheritance
class Parent:
    x=10
    def __init__(self,name):
        self.n=name

    def home(self):
        print("HEllo")

class Child(Parent):
    x=20
    def home(self):
        print("Hello from home class")
        super().home()


obj=Child("aditya")
print(obj.x)
print(obj.n)
obj.home()

# Multilevel
class Gparent:
    def car(self):
        print("XYZ")

class Parent(Gparent):
    x=10
    def __init__(self,name):
        self.n=name

    def home(self):
        print("HEllo")

    def car(self):
        print("ABC")
        super().car()

    

class Child(Parent):
    x=20
    def home(self):
        print("Hello from home class")
        super().home()


obj=Child("aditya")
print(obj.x)
print(obj.n)
obj.home()
obj.car()

# Multiple Inheritance
# class Parent:
#     def car(self):
#         print("XYz")

# class Parent1:
#     x=20
#     def home(self):
#         print("Hello from home class")
        

# class Child(Parent,Parent1):
#     x=20
#     def home(self):
#         print("Hello from home class")
        


# obj=Child("aditya")
# print(obj.x)
# print(obj.n)
# obj.home()


# Heirarcical
class Parent:
    x=10
    def __init__(self,name):
        self.n=name

    def home(self):
        print("HEllo")

class Child1(Parent):
    def home(self):
        print("HEllo")
        super().home()

class Child2(Parent):
    pass

obj1=Child2("Python")
obj2=Child1("Java")
obj1.home()
print(obj1.n,obj2.n)

# Hybrid Inheritance
# Method Resolution Order (MRO):- Depth first algo are used
class A:
    def first(self):
        print("from class A")

class B:
    def first(self):
        print("from class B")

class C(A):
    pass

class D(B):
    pass

class E(A,B):
    pass

obj=E()
obj.first()

