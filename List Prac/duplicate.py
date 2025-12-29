def removeduplicate(li):
    li=set(li)
    li=list(li)
    li.sort()
    return len(li)

print(removeduplicate([2,2,4,6,6,9,2]))