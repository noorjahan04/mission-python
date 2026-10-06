def calculator(a,b,operation):
    if(operation=="+"):
        return a+b
    elif(operation=="-"):
        return a-b
    elif(operation=="*"):
        return a*b
    elif(operation=="/"):
        return a/b
    else:
        return "Invalid operation"

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
operation=input("Enter operation:")
print("Result:", calculator(a,b,operation))