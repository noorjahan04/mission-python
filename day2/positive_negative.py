while True:
    n=input("Enter a number or Quit:")
    if n=="Quit":
        break
    n=int(n)
    if(n>0):
        print("Positive")
    elif(n<0):
        print("Negative")
    else:
        print("Zero")