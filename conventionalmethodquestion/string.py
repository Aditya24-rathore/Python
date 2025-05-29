s='python'
l=list(s)
l[0],l[5]=l[5],l[0]
s="".join(l)
print(s)
