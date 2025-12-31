# Encapsulation:-bind multiple variables and method in single class
# public variable
class P:
    x=10
    def show(self):
        print("from p class")

class C(P):
    pass

obj=C()
print(obj.x)
print(obj.show())

# protected variable:- not supported in python(it can access only in     their child  class)
# name magle is used to change name
class P:
    x=10
    def _show(self):
        print("from p class")

class C(P):
    pass

obj=C()
print(obj.x)
print(obj._show())

# private variable:- it can access only in their parent class

class P:
    __x=10
    def __show(self):
        print("from p class")

class C(P):
    pass

print(dir(C))
obj=C()
print(obj._P__show())
