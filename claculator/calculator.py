while True:
    print("1.add \n 2.subt \n 3.mul 4.off")
    n=int(input("enter value"))
    x=(1,2,3,4)
    if n in x:
        if n==1:
            p=int(input("enter value"))
            q=int(input("enter value"))
            print(p+q)
        elif n==2:
            p=int(input("enter value"))
            q=int(input("enter value"))
            print(p-q)
        elif n==3:
            p=int(input("enter value"))
            q=int(input("enter value"))
            print(p*q)
        elif n==4:
            break
    else:
        print("enter correct value")