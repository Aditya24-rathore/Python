while True:
    print("1.add \n 2.subt \n 3.mul \n 4.off ")
    n=int(input("enter option "))
    x=(1,2,3,4)
    if n in x:
        if n==1:
            p=int(input("enter first value for addition"))
            q=int(input("enter second value for addition"))
            print(p+q)
        elif n==2:
            p=int(input("enter first  value for substraction"))
            q=int(input("enter second value for subtraction"))
            print(p-q)
        elif n==3:
            p=int(input("enter first  value for multiplication"))
            q=int(input("enter second value for multiplication"))
            print(p*q)
        elif n==4:
            break
    else:
        print("enter correct value")