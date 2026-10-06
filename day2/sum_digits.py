def sum(n):
    total=0
    for digit in str(n):
        total+=int(digit)
    return total

n=int(input("Enter a number:"))
print(sum(n))