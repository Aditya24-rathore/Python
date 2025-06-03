# f=open("n.py",'a')
# l=["this is python class\n","this is python class\n"]
# f.writelines(l)
# f.close()

# f=open("n.py")
# data=f.read()
# print(data)
# f.close()

# f=open("n.py")
# data=f.read(1000000)
# print(data)
# f.close()

# f=open("n.py")
# data=f.readline()
# print(data)
# f.close()

# f=open("n.py")
# data=f.readlines()
# print(data)
# print(type(data))
# f.close()


# cursor position
# f=open("n.py")
# print(f.tell())
# data=f.read(10)
# print(data)
# print(f.tell())
# f.close()

# cursor moment
f=open("n.py",'rb')
print(f.tell())
data=f.read(10)
print(data)
print(f.tell())
f.seek(5)
print(f.tell())
data=f.read(5)
print(data)
print(f.tell())