l=[1,6,7,4,7]
target=11
stop_loop=False
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==target:
            print(i,j)
    