n=int(input("enter number"))
i=1
while i<=n:
    if i<(n-1):
        print(i,end=',')
    else:
        print(i)
    i=i+2

# sum of odd number
n=int(input("enter number"))
i=1
sum=0
while i<=n:
    sum=sum+i
    if i<(n-1):
        print(i,end=',')
    else:
        print(i,end='=')
    i=i+2
print(sum)