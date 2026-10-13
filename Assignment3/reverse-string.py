string=input("Enter a String: ")
reverse=""
for ch in string:
    reverse=ch+reverse

if string==reverse:
    print("It is a palindrom")
else:
    print("It is not a palindrom")