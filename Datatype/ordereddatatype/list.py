# list is a collection of homogenous as well as hetrogenous elements.
# list inbuit function
l=[2,4,6,8,]
print(max(l))
print(min(l))
print(len(l))
print(sum(l))
print(type(l))
print(id(l))

# List method
# append - add element in last
l=[10,20,30,40]
l.append(50)
print(l)

# extend - add multiple element in last
t=(50,60,70)
l=[10,20,30,40]
l.extend(t)
print(l)

# insert - target one element and add
l=[10,20,30,40]
l.insert(2,"python")
print(l)

l=[10,20,30,40]
l.insert(3,t)
print(l)

l=[10,20,30,40]
l.insert(8,50)
print(l)

# pop - remove last element
l=[10,20,30,40]
l.pop()
print(l)
print(l.pop())

l=[10,20,30,40]
l.pop(0)
print(l)
print(l.pop(0))

# remove - target specific element and remove
l=[10,20,30,40]
l.remove(40)
print(l)

# index - find element index number
l=[10,20,30,40]
print(l.index(20))

# count - count repetation of element
l=[10,20,30,40,20]
print(l.count(20))

# reverse - reverse the element
l=[1,4,6,"python","java"]
l.reverse()
print(l)

# sort - sort element in ascending order
l=[10,20,50,80]
l.sort(reverse="true")
# l.reverse()
print(l)

l=["Php","php","Java"]
l.sort()
print(l)

# copy - create new object of same element
l=["Php","php","Java"]
l1=l.copy()
print(id(l1),id(l))

# clear - clear all the element in the list and give empty list
l=["Php","php","Java"]
l.clear()
print(l)

# del is predefined variable used to free the memory
l=["Php","php","Java"]
del l
print(l)