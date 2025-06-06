# generator creates a collection in more controlled way
def natural_no(x):
    i=1
    while i<=x:
        yield i
        i=i+1

x=int(input("enter number"))
x=natural_no(x)
# for i in x:
#     print(i)
print(next(x))
