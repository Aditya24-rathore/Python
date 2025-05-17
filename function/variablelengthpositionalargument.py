def fibo(*n):
    print(n)
    print(type(n))

fibo(1,2,3,4)

# sum of number
def sum(*n):
    sum=0
    for i in n:
        sum=sum+i
        print(i)
    return sum

x=sum(10,20,30)
print(x)

# keyword argument
def sub(**n):
    print(n)
    print(type(n))

sub(name="aditya",age=24,)


def new(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
new(name="aditya",age=24,)

def new(**kwargs):
    for k in kwargs.keys():
        print(k)
new(name="aditya",age=24,)