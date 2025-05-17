l=(1,2,3,4,5)
def add5(n):
    return n+5

x=map(add5,l)
print(x)
print(tuple(x))
print(list(x))
print(type(x))


# sum of number 
l1=(1,4,5,6,7)
l2=(6,7,8,7,5)
def add5(z,y):
    return z+y

a=map(add5,l1,l2)
print(list(a))


# power of number 
l1=(1,4,5,6,7)
l2=(6,7,8,7,5)
def add5(z,y):
    return z**y

a=map(add5,l1,l2)
print(list(a))