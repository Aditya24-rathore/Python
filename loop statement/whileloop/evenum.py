n=int(input("enter number"))
i=2
while i<=n:
    if i<(n-1):
        print(i,end=',')
    else:
        print(i)
    i=i+2

# even number upto 10
num=10
i=2
while i<=num:
    if i<(num-1):
        print(i,end=',')
    else:
        print(i)
    i=i+2

# sum of an even number upto 10
num=10
i=2
sum=0
while i<=num:
    sum=sum+i
    if i<(num-1):
        print(i,end='+')
    else:
        print(i,end='=')
    i=i+2
print(sum)

# sum of an even number upto user input
num=int(input("enter number"))
i=2
sum=0
while i<=num:
    sum=sum+i
    if i<(num-1):
        print(i,end='+')
    else:
        print(i,end='=')
    i=i+2
print(sum)
