d={}

# Dictionary method
# Copy - used to create new object
d={"name":"aditya","age":20}
d1=d.copy()
print(d,d1)
print(id(d),id(d1))

# clear
d={"name":"aditya","age":20}
d.clear()
print(d,d1)
print(id(d),id(d1))

# del
# d1={"name":"aditya","age":20}
# del d1
# print(d1)

# pop
d={"name":"aditya","age":20}
d.pop("name")
print(d)

# pop item
d={"name":"aditya","age":20}
d.popitem()
print(d)

# get
d={"name":"aditya","age":20}
new=d.get("name")
print(new)

# values
d={"name":"aditya","age":20}
print(d.values())

# keys
d={"name":"aditya","age":20}
print(d.keys())

# items
d={"name":"aditya","age":20}
print(d.items())

# fromkeys
s="python"
d2=dict.fromkeys(s)
print(d2)

l=["python","java","php"]
d2=dict.fromkeys(l,10)
print(d2)

# setdefault
d={"name":"aditya","age":20}
d.setdefault("name2","aditya")
print(d)

# uodate
d={"name":"aditya","age":20}
d1={"qual":"B.tech"}
d.update(d1)
print(d,d1)