# set - A collection of unique element
        # unordered collection
        # indexing not supported
        # slicing not supported
        # mutable in nature
        # represented in {} with , seperated
        # duplicate not allowed


s={10,50,30,40,40,"python","java"}
print(s)
print(type(s))
print(id(s))

# python inbuilt function applicable on set
# length
s={10,50,30,40,40,"python","java"}
print(len(s))

# maximum
s={10,50,30,40,40}
print(max(s))

s1={"python","Cpp","java"}
print(max(s1))

# mimimum
s={10,50,30,40,40}
print(min(s))

s1={"python","Cpp","java"}
print(min(s1))

# sum - only numberic value
s={10,50,30,40,40}
print(sum(s))

# type
s={10,50,30,40,40}
print(type(s))

# id
s={10,50,30,40,40}
print(id(s))


# Set Method
# add - used to add single element randomly
s={10,50,30,40,40}
# s.add(60)
print(s)

# update - used to add multiple element randomly
s={10,50,30,40,40}
s.update(["python","java"])
print(s)

s={10,50,30,40,40}
s.update("python","java")
print(s)

s={10,50,30,40,40}
s.update(("python","java"))
print(s)

s={10,50,30,40,40}
s.update({"python","java"})
print(s)

# pop - remove element randomly
s={10,50,30,40,40}
s.pop()
print(s)

s={10,50,30,40,40}
print(s.pop())

# remove - remove the targeted element or show error
s={10,50,30,40,40}
s.remove(40)
print(s)

# discard - cannot show error
s={10,50,30,40,40}
s.discard(50)
print(s)

# copy - copy the element but different id address
s={10,50,30,40,40}
new=s.copy()
print(id(s),id(new))

# clear - clear all the element but empty set remain
s={10,50,30,40,40}
s.clear()
print(s)

# empty set declare
s1=set()
print(s1)

# empty variable declare
x=int()
y=str()
z=complex()
a=float()
b=list()
c=tuple()
print(x,z,a,b,c)
print(y)

# typecasting
n=input("enter any value")
d=list(n)
e=tuple(n)
f=set(n)
g=frozenset(n)
# typecasting is not possible in dictionary(it has key and value pair)
h=dict.fromkeys(n)
print(d,e,f,g,h)


dict={"name":"aditya","age":20}
type=list(dict)
str=list(dict)
print(type,str)