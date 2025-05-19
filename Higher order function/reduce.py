# greater number from list
from functools import reduce
l=[2,10,12,20]
def max_no(x,y):
    if x>y:
        return x
    else:
        return y
    
x=reduce(max_no,l)
print(x)

# smaller number from list
from functools import reduce
l=[2,10,12,20]
def max_no(x,y):
    if x<y:
        return x
    else:
        return y
    
x=reduce(max_no,l)
print(x)


# sum of number from list
from functools import reduce
l=[2,10,12,20]
def sum(x,y):
    return x+y
    
    
x=reduce(sum,l)
print(x)


