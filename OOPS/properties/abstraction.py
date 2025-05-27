# Abstraction
# Abstract class:- inherit ABC module
# Abstract method:- it has name and their body are empty
# Concrete method

from abc import ABC, abstractmethod
class Senior(ABC):
    def add(self,x,y):
        print(x+y)

    def sub(self,x,y):
        print(x-y)

    def mul(self,x,y):
        print(x*y)

    @abstractmethod
    def div(self):
        pass

class Junior(Senior):
    def div1(self,x,y):
        print(x/y)

obj=Junior()
obj.div(5,10)
obj.add(10,10)
