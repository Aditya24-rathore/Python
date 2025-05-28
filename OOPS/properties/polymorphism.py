# Overload not supported by python
class Student:
    def __init__(self):
        print("Hello from student")

    def __init__(self,x,y,z):
        print("Hello from class")

obj=Student()


