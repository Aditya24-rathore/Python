# n=input("enter name")
# if n.replace(' ','') and n.isalpha():
#     print(n)
# else:
#     print("please enter correct name")

e=input("enter email")
if e[0].isalpha() and e.endswith("@email.com"):
    print(e)
else:
    print("enter correct email")