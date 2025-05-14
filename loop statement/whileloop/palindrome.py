# palindrome using inbuilt function
'''n=input("enter value")
if n==n[::-1]:
    print(f'{n} is palindrome')
else:
    print(f'{n} is not a palidrome')'''


s=input("enter value")
l=len(s)
s1=''
i=-1
while l>0:
    x=s[i]
    s1="".join((s1,x))
    i=i-1
    l=l-1
print(s1)
if s==s1:
    print(f'given string is palindrome')
else:
    print(f'given string is not an palindrome')