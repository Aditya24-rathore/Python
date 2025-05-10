# palindrome using inbuilt function
'''n=input("enter value")
if n==n[::-1]:
    print(f'{n} is palindrome')
else:
    print(f'{n} is not a palidrome')'''


n=int(input("enter number"))
r=0
k=n
while n>0:
    r=r*10+n%10
    n=n/10
if r==k:
    print("palindrome")
else:
    print("not an palindrome")