# Overload not supported by python
# Polymorphism allows different classes to use the same method name with different behavior.
# pyhton does not support compile time polymorphism

class Student:
    def __init__(self):
        print("Hello from student")

    def __init__(self,x,y,z):
        print("Hello from class")

obj=Student()


