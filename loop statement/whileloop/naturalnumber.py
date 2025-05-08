n=int(input("enter number"))
i=1
while i<=n:
    print(i,end=', ',sep=',')
    i=i+1

n=int(input("enter number"))
i=1
while i<=n:
    if i<=(n-1):
        print(i,end=',')
    else:
        print(i)
    i=i+1

# sum of natural number
n=int(input("enter number"))
i=1
sum=0
while i<=n:
    sum=sum+i
    if i<=(n-1):
        print(i,end=',')
    else:
        print(i,end='=')
    i=i+1
print(sum)

# multiplication of natural number
n=int(input("enter number"))
i=1
multiplication=1
while i<=n:
    multiplication=multiplication*i
    if i<=(n-1):
        print(i,end='+')
    else:
        print(i,end='=')
    i=i+1
print(multiplication)