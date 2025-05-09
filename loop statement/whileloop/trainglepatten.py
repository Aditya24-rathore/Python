'''n=int(input("enter number"))
i=1
while i<=n:
    print('*'*i)
    i=i+1


n=int(input("enter number"))
i=1
while i<=n:
    print(" "*(n-i)+'*'*i)
    i=i+1


n=int(input("enter number"))
i=1
while i<=n:
    print(" "*(n-i)+'* '*i)
    i=i+1


n=int(input("enter number"))
i=0
while i<n:
    print(" "*i+' * '*(n-i))
    i=i+1

n=int(input("enter number"))
i=0
while i<n:
    print(" "*i+' *'*(n-i))
    i=i+1'''


n=int(input("enter number"))
while n>0:
    print('*'*n)
    n=n-1