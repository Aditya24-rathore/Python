# def naturalno(n):
#     for i in range(1,n+1):
#         print(i)
# x=int(input("enter number"))
# naturalno(x)

# Sum of natural number
def sumnaturalno(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
        print(i)
    print(sum)
x=int(input("enter number"))
sumnaturalno(x)

# While loop
def n_no(x):
    i=1
    sum=0
    while i<=x:
        sum=sum+i
        if i<=(x-1):
            print(i,end=",")
        else:
            print(i,end="=")
        i=i+1
    print(sum)
        

n=int(input("enter number"))
n_no(n)