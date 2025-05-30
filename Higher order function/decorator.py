# decorator can be represented by @ symbol in python
def outer_fun(main_func):
    def inner_func(p,q):
        p=p+5
        q=q+5
        r=main_func(p,q)
        return r
    return inner_func

@outer_fun
def add(a,b):
    return a+b

z=add(10,20)
print(z)