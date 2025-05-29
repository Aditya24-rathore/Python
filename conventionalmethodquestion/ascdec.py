#accending
l = [10,2,4,6,8,20]

for i in range(len(l)):
    swapped = 0

    for j in range(0,len(l)-1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1],l[j]
            swapped = 1
    
    if not swapped == 1:
        break

print(l)

#decending
l = [10,2,4,6,8,20]

for i in range(len(l)):
    swapped = 0

    for j in range(0,len(l)-1):
        if l[j] < l[j + 1]:
            l[j], l[j + 1] = l[j + 1],l[j]
            swapped = 1
    
    if not swapped == 1:
        break

print(l)

#max
l = [10,2,4,6,8,20]
max_value = l[0]

for i in range(len(l)):
    if l[i] > max_value:
        max_value = l[i]

print('maximum value is',max_value)

#min
l = [10,2,4,6,8,20]
max_value = l[0]

for i in range(len(l)):
    if l[i] < max_value:
        max_value = l[i]

print('minimum value is',max_value)