# greater number
l=[1,2,3,4,5,6,7,8]
def evenno(n):
    if n>=5:
        return n
   
x=filter(evenno,l)
print(x)
print(tuple(x))

# even num
l=[1,2,3,4,5,6,7,8]
def evenno(n):
    if n%2==0:
        return n
   
x=filter(evenno,l)
print(x)
print(tuple(x))

# conventional method to find greater number 
l1=[1,2,3,4,5,6,7,8]
l2=[]
for i in l:
    if i>=5:
        l2.append(i)
print(l2)