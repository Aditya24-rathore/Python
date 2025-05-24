# instance method :- First parameter is self
# Class method :- First parameter is cls
class Student:
    school="XYZ"
    grade=10
    def __init__ (self,name):
        self.n=name
    def showdetails(self):
        print(self.n)
        print(Student.school)
        print(Student.grade)
    @classmethod
    def updategrade(cls,updated):
        cls.grade=updated


    

obj=Student("Adi")
obj.showdetails()
Student.updategrade('11')
obj2=Student("aditya")
obj2.showdetails()


# static method
class Student:
    school="XYZ"
    grade=10
    def __init__ (self,name):
        self.n=name
    def showdetails(self):
        print(self.n)
        print(Student.school)
    @staticmethod
    def addnew(cls,self,city):
        print(self)
        print(cls)
        print(city)
obj=Student("Adi")
obj.showdetails()
obj2=Student("aditya")
obj2.showdetails()
Student.addnew("Bhopal","Indore","Sehore")
obj.showdetails()

