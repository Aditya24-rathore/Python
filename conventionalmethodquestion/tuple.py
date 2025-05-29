t=(2,3,1,0,5)
l=list(t)
l[0],l[4]=l[4],l[0]
t=tuple(l)
print(t)