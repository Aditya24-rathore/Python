'''s=input("enter string")
for i in s:
    print(i)

t=eval(input("enter tuple"))
for i in t:
    print(i)

d={1:"python",2:"java"}
for k,v in d.items():
    print(k,'=',v)
for k in d.keys():
    print(k)
for v in d.values():
    print(v)

n=int(input("enter range"))
for i in range(1,n+1):
    print(i)

n=int(input("enter range"))
for i in range(2,n+1,2):
    print(i)

n=int(input("enter range"))
sum=0
for i in range(1,n+1,2):
    sum=sum+i
    print(i,end=",")
print(sum)'''

n=int(input("enter range"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print(i,end=",")
print(sum)


