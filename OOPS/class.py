# real world entity is converted into programming world is knowns as oops
# class,object,constructor,self
# class is a dammymodel,template,blueprint of any real world entity
# the physical existence of class is known as object


class First:
    pass
print(id(First))

obj=First
print(id(obj))

obj1=First()
print(id(obj1))                         

# constructor is method it is call automatically object is call.
class first:
    def __init__ (self):
        print("constructor called")
        print(id(self))

obj=first
obj=first()
print(id(obj))

# self is a refrence variable it hold the address of current object

class student:
    def __init__(self,name,city,phone):
        self.n=name
        self.c=city
        self.p=phone

obj=student("aditya","sehore",1111)
obj1=student("adi","bhopal",2222)
print(obj.n,obj.c,obj.p)
print(obj1.n,obj1.c,obj1.p)

# variable:- it is a container that hold the value
# instance variable :- it depend on the object
class studentdata:
    def __init__(self,name,city):
        self.n=name
        self.c=city
        print(self.n,self.c)

    def add(self,phone):
        self.p=phone
        print(self.p,obj2.school,self.n,self.c)

obj2=studentdata("adi","sehore")
obj2.school="st mary"
obj2.add(1234)
print(obj2.n,obj2.p,obj2.c,obj2.school)
        
# class/static variable:- do not depend on object
class Student:
    school="XYZ"
    def __init__ (self,name):
        self.n=name
        Student.schoolcode=101
    def addnew(self):
        Student.schoolcity="Bhopal"
        print(Student.schoolcity)

    def display(self):
        print(Student)
        print(Student.school)
        print(self.n)
        print(Student.schoolcity)
        print(Student.grade)

Student.grade="10"
obj=Student("aditya")
obj1=Student("adi")
print(obj.school)
print(obj1.school,obj1.n)
print(Student.school)
obj.addnew()
obj.display()

# local variable:-scope dependent
class students:
    def __init__(self,name):
        grade="20"
        self.name=name
        print(grade)

    def grade(self):
        print(grade)
        
obj=students("anuuu")
obj.grade()