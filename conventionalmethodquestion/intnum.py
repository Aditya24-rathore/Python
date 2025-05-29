n=12345
s=str(n)
l=list(s)
l[0],l[-1]=l[-1],l[0]
s="".join(l)
n=int(s)
print(n)
print(type(n))