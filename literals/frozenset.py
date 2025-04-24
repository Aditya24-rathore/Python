S={10,20,30,10,'java','python','java'}
x=frozenset(S)
print(x)
print(type(x))


x='python'
x=frozenset(x)
print(x)
print(type(x))