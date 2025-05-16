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