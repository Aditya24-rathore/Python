n=int(input("enter number"))
x,y,i=0,1,1
while i<=n:
    z=x+y
    if i<n:
        print(z,end=',')
    else:
        print(z)
    x,y=y,z
    i=i+1