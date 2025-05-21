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

