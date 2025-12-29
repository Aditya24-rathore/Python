# s="Anagram"
# data={}
# for i in s:
#     data[i]=data.get(i,0)+1
# print(data)

s1="Anagram"
s2="red"
if len(s1)!=len(s2):
    print("not anagram")
else:
    d1={}
    for i in d1:
        d1[i]=d1.get(i,0)+1
    for j in d1:
        d1[j]=d1.get(j,0)-1
    for i in d1.values():
        if i!=0:
            pass