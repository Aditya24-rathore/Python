
val = eval(input("Enter value : "))

if type(val) == type(int()) :
    print(f"Given value {val} is integer.")
elif type(val) == type(float()) :
    print(f"Given value {val} is float.")
elif type(val) == type(complex()):
    print(f"Given value {val} is complex.")
elif type(val) == type(str()) :
    print(f"Given value {val} is string.")
elif type(val) == type(list()) :
    print(f"Given value {val} is list.")
elif type(val) == type(tuple()):
    print(f"Given value {val} is tuple.")
elif type(val) == type(set()) :
    print(f"Given value {val} is set.")
elif type(val) == type(dict()) :
    print(f"Given value {val} is dictionary.")
else :
    print(f"Given program will not run!")