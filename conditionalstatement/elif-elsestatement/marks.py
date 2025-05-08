h,e,m=int(input("enter your number")),int(input("enter your number")),int(input("enter your number"))
if(h>=0 and h<=100 and e>=0 and e<=100 and m>=0 and m<=100):
    avg=h+e+m/3
    if(avg>=60 and avg<=100):
        print(f'{avg} pass with first division')
    elif(avg>=59 and avg>=45):
        print(f'{avg} pass with second division')
    elif(avg>=44 and avg>30):
        print(f'{avg} pass with third division')
    else:
        print(f'{avg} you are fail')
else:
    print("enter valid number")