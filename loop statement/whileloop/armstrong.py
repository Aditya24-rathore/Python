n=int(input("enter number"))
x=y=n
digit=0
sum=0
while n>0:
    digit=digit+1
    n=n//10
while x>0:
    lastdigit=x%10
    sum=sum+lastdigit**digit
    x=x//10
# print(sum)
# print(x)
if y==sum:
    print(f'{y} is a armstrong')
else:
    print(f'{y} is not a armstrong')
    