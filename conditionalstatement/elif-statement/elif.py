# greater between three number
a,b,c=int(input("enter number")),int(input("enter number")),int(input("enter number"))

if(a>b and a>c):
    print(f'{a} is greater')
elif(b>a and b>c):
    print(f'{b} is greater')
elif(c>a and c>b):
    print(f'{c} is greater')    